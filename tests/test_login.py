from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

def test_TC_LOG_01_login_success(login_page: LoginPage, page):
    login_page.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.verify_url("https://www.saucedemo.com/inventory.html")
    
def test_TC_LOG_02_login_wrong_password(login_page: LoginPage):
    login_page.login("standard_user", "secretasd")
    login_page.verify_error_msg("Username and password do not match")
    
def test_TC_LOG_03_login_locked_user(login_page: LoginPage):
    login_page.login("locked_out_user", "secret_sauce")
    login_page.verify_error_msg("Sorry, this user has been locked out")
    
def test_TC_log_04_login_empty_field(login_page: LoginPage):
    login_page.login ("", "")
    login_page.verify_error_msg("Username is required")
    
def test_TC_log_05_logout(logged_in_inventory: InventoryPage):
    logged_in_inventory.logout()
    logged_in_inventory.verify_url("https://www.saucedemo.com/")
