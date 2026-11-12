from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.post_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.error_message = page.locator('[data-test="error"]')
        self.overview_items = page.locator('[data-test="inventory-item-name"]')
        self.complete_header = page.locator('[data-test="complete-header"]')
        
    def fill_information(self, first_name: str = "",last_name: str = "", postal_code: str = ""):
        if first_name: self.first_name_input.fill(first_name)
        if last_name: self.last_name_input.fill(last_name)
        if postal_code: self.post_code_input.fill(postal_code)
        self.continue_button.click()
        
    def finish_checkout(self):
        self.finish_button.click()

    def click_cancel_on_info(self):
        self.cancel_button.click()
        
    def verify_overview_items(self, expected_items: list[str]):
        expect(self.overview_items).to_have_count(len(expected_items))
        expect(self.overview_items).to_have_text(expected_items)
    
    def verify_order_sukses(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")
        
    def verify_error_msg(self, expected_text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)
