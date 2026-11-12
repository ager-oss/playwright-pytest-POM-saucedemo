from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_item_names = page.locator('[data-test="inventory-item-name"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.remove_buttons = page.get_by_role("button", name="Remove")
        
    def verify_cart_items(self, expected_items: list[str]):
        expect(self.cart_item_names).to_have_count(len(expected_items))
        expect(self.cart_item_names).to_have_text(expected_items)
        
    def remove_all_items(self):
        while self.remove_buttons.count() > 0:
            self.remove_buttons.first.click()
            
    def click_checkout(self):
        self.checkout_button.click()
        
