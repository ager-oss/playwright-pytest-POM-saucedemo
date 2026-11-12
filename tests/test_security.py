from pages.LoginPage import LoginPage


def test_TC_LOG_01_direct_access_inventory_page_without_login(login_page: LoginPage):
    """TC-SEC-01: Memastikan user tanpa login dilarang masuk ke inventory."""
    login_page.navigate_to("https://www.saucedemo.com/inventory.html")
    login_page.verify_error_msg("Epic sadface: You can only access '/inventory.html' when you are Logged in.")


def test_TC_LOG_02_direct_access_checkout_without_login(login_page: LoginPage):
    """TC-SEC-02: Memastikan user tanpa login dilarang masuk ke checkout."""
    login_page.navigate_to("https://www.saucedemo.com/checkout-step-one.html")
    login_page.verify_error_msg("Epic sadface: You can only access '/checkout-step-one.html' when you are Logged in.")
    
      
    