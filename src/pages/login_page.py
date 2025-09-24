
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.config import BASE_URL

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN    = (By.ID, "login-button")

    def go(self):
        return self.open(BASE_URL)

    def login_as(self, username: str, password: str):
        self.wait.until_visible(*self.USERNAME).send_keys(username)
        self.wait.until_visible(*self.PASSWORD).send_keys(password)
        self.wait.until_clickable(*self.LOGIN).click()
        return self
