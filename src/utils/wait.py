
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Waiter:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def until_visible(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def until_clickable(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, locator))
        )

    def until_present(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def until_text(self, by, locator, text):
        WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element((by, locator), text)
        )
        
    def until_url_contains(self, fragment: str):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(fragment)
        )

    @staticmethod
    def by_css(selector: str):
        return (By.CSS_SELECTOR, selector)
