
from src.utils.wait import Waiter
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = Waiter(driver)

    def open(self, url: str):
        self.driver.get(url)
        return self
    
    def ensure_ready(self):
        """
        Wait until load page
        """
        WebDriverWait(self.driver, self.wait.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def go(self, url: str):
        """
        go to 'url'
        """
        self.driver.get(url)
        self.ensure_ready()
        return self
