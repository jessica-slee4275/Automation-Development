from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

def _slug(name: str) -> str:
    return name.strip().lower().replace(" ", "-")

class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.ID, "shopping_cart_container")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart-{}']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-test='remove-{}']")
    
    MENU_BTN   = (By.ID, "react-burger-menu-btn")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    CLOSE_MENU = (By.ID, "react-burger-cross-btn")
    
    def reset_app_state(self):
        self.wait.until_clickable(*self.MENU_BTN).click()
        self.wait.until_clickable(*self.RESET_LINK).click()
        self.wait.until_clickable(*self.CLOSE_MENU).click()
        return self
    
    def add_item_by_name(self, name: str):
        """ 
        if items are in the cart, pass
        if not, add
        """
        self.ensure_ready()
        slug = _slug(name)

        add_loc = (self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1].format(slug))
        remove_loc = (self.REMOVE_BUTTON[0], self.REMOVE_BUTTON[1].format(slug))

        # pass if items are in the cart
        if self.driver.find_elements(*remove_loc):
            return self

        # click add btn if items are not in the cart
        self.wait.until_present(*add_loc)
        self.wait.until_visible(*add_loc)
        btn = self.driver.find_element(*add_loc)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        self.wait.until_clickable(*add_loc).click()
        return self

    def remove_item_by_name(self, name: str):
        self.ensure_ready()
        slug = _slug(name)
        remove_loc = (self.REMOVE_BUTTON[0], self.REMOVE_BUTTON[1].format(slug))
        if self.driver.find_elements(*remove_loc):
            btn = self.wait.until_present(*remove_loc)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            self.wait.until_clickable(*remove_loc).click()
        return self

    def open_cart(self):
        self.wait.until_clickable(*self.CART_LINK).click()
        return self
