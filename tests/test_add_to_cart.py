
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage

def test_add_and_remove_cart(driver):
    LoginPage(driver).go().login_as("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.reset_app_state()

    inv.add_item_by_name("Sauce Labs Backpack")
    inv.add_item_by_name("Sauce Labs Bike Light")

    inv.open_cart()
    cart = CartPage(driver)
    assert cart.has_item("Sauce Labs Backpack")
    assert cart.has_item("Sauce Labs Bike Light")
