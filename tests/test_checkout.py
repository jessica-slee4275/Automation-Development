
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    LoginPage(driver).go().login_as("standard_user", "secret_sauce")
    inv = InventoryPage(driver)
    inv.add_item_by_name("Sauce Labs Backpack").open_cart()

    cart = CartPage(driver)
    cart.go_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_shipping("Jess", "Lee", "M5G1X1").finish()
    assert checkout.is_complete()
