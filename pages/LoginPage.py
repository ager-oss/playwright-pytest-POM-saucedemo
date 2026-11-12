import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_msg = page.locator('[data-test="error"]')

    def login(self, username:str, password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_error_msg(self, expected_test:str):
        expect(self.error_msg).to_be_visible()
        expect(self.error_msg).to_contain_text(re.compile(re.escape(expected_test), re.IGNORECASE))
        
    
        