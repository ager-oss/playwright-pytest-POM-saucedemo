from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.app_logo = page.locator(".app_logo")
        self.product_cards = page.locator('[data-test="inventory-item"]')
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        self.product_prices = page.locator('[data-test="inventory-item-price"]')
        self.sort_dropdown = page.locator('[data-test = "product-sort-container"]')
        self.cart_link = page.locator('[data-test = "shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test = "shopping-cart-badge"]')
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator('[data-test = "logout-sidebar-link"]')
    
    def add_first_n_items(self, count: int) -> list[str]:
        added_names = []
        for i in range(count):
            added_names.append(self.product_names.nth(i).inner_text())
            self.product_cards.nth(i).get_by_role("button", name="Add to cart").click()
        return added_names
    
    def add_item_by_name(self, name: str):
        product = self.product_cards.filter(has_text=name)
        product.get_by_role("button", name="Add to cart").click()
        
    def sort_product(self, option_value:str):
        self.sort_dropdown.select_option(option_value)
        
    def get_all_product_names(self) -> list[str]:
        return self.product_names.all_text_contents()
    
    def get_all_product_prices(self) -> list[float]:
        raw_prices = self.product_prices.all_text_contents()
        return[float(price.replace("$", "")) for price in raw_prices]
    
    def go_to_cart(self):
        self.cart_link.click()
        
    def logout(self):
        expect(self.app_logo).to_be_visible()
        self.burger_menu.click()
        self.logout_link.click()
        
    def verify_cart_badge_count(self, expected_count: int):
        if expected_count > 0:
            expect(self.cart_badge).to_have_text(str(expected_count))
        else:
            expect(self.cart_badge).not_to_be_visible()
            
    def remove_item_by_name(self, name:str):
        product = self.product_cards.filter(has_text=name)
        product.get_by_role("button", name= "Remove").click()
        
    def click_product_name(self, name:str):
        self.product_names.filter(has_text=name).click()
        
            
