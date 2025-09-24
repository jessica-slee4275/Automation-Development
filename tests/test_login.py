
import os
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage

def test_login_valid_user(driver):
    login = LoginPage(driver).go()
    login.login_as("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    # Assert inventory page loaded
    assert "inventory" in driver.current_url
