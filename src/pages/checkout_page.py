
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST = (By.ID, "first-name")
    LAST  = (By.ID, "last-name")
    ZIP   = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH   = (By.ID, "finish")
    COMPLETE = (By.CSS_SELECTOR, ".complete-header")

    def fill_shipping(self, first: str, last: str, zip_code: str):
        self.wait.until_visible(*self.FIRST).send_keys(first)
        self.wait.until_visible(*self.LAST).send_keys(last)
        self.wait.until_visible(*self.ZIP).send_keys(zip_code)
        self.wait.until_clickable(*self.CONTINUE).click()
        return self

    def finish(self):
        self.wait.until_clickable(*self.FINISH).click()
        return self

    def is_complete(self) -> bool:
        return self.wait.until_visible(*self.COMPLETE).is_displayed()
