
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")

    def has_item(self, name: str) -> bool:
        try:
            self.wait.until_visible(By.XPATH, f"//div[@class='cart_item']//div[text()='{name}']")
            return True
        except Exception:
            return False

    def go_checkout(self):
        self.wait.until_clickable(*self.CHECKOUT_BTN).click()
        return self
