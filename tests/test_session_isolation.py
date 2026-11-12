from playwright.sync_api import Browser, Page, expect
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

def test_TC_SYS_01_multi_user_session_isolation(browser: Browser):
    """dua user login bareng di browser berbeda tanpa mengganggu satu sama lain"""
    #context untuk user 1
    context1 = browser.new_context()
    page1 = context1.new_page()
    login1 = LoginPage(page1)
    login1.navigate_to("https://www.saucedemo.com")
    login1.login("standard_user", "secret_sauce")
    inv1 = InventoryPage(page1)
    inv1.add_first_n_items(2)
    inv1.verify_cart_badge_count(2)
    
    #contect untuk user 2
    context2 = browser.new_context()
    page2 = context2.new_page()
    login2 = LoginPage(page2)
    login2.navigate_to("https://www.saucedemo.com")
    login2.login("standard_user", "secret_sauce")
    inv2 = InventoryPage(page2)
    
    #pastikan keranjang user 2 masih bersih (0), tidak terpengaruh user 1
    inv2.verify_cart_badge_count(0)
    
    #cleanup context
    context1.close()
    context2.close()
    