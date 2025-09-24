import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from src.utils.config import BROWSER, HEADLESS, CI
from src.utils.logger import get_logger

logger = get_logger("conftest")

@pytest.fixture(scope="session")
def driver():
    if BROWSER == "firefox":
        options = FirefoxOptions()
        if HEADLESS or CI:
            options.add_argument("-headless")
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        drv = webdriver.Firefox(service=service, options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        options.add_argument("--disable-infobars")
        if "incognito" in BROWSER:  # secret mode
            options.add_argument("--incognito")
        if HEADLESS or CI:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(executable_path=ChromeDriverManager().install(), log_output=os.devnull)
        drv = webdriver.Chrome(service=service, options=options)

    drv.set_window_size(1280, 900)
    yield drv
    drv.quit()

def pytest_runtest_makereport(item, call):
    # Attach screenshot on failure
    if call.when == "call" and call.excinfo is not None:
        drv = item.funcargs.get("driver")
        if drv:
            os.makedirs("artifacts", exist_ok=True)
            path = f"artifacts/{item.name}.png"
            drv.save_screenshot(path)
            logger.info(f"Saved screenshot: {path}")
