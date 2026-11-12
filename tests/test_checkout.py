from playwright.sync_api import Page
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

def test_TC_CHK_01_checkout_place_order_sukses(logged_in_inventory: InventoryPage, page: Page):
    added_items = logged_in_inventory.add_first_n_items(5)
    logged_in_inventory.go_to_cart()
    
    cart = CartPage(page)
    cart.click_checkout()
    
    checkout = CheckoutPage(page)
    checkout.fill_information("singgih", "ager", "12345")
    checkout.verify_overview_items(added_items)
    checkout.finish_checkout()
    
    checkout.verify_order_sukses()
    logged_in_inventory.verify_cart_badge_count(0)
    
def test_TC_CHK_02_checkout_empty_field(logged_in_inventory: InventoryPage, page: Page):
    logged_in_inventory.add_first_n_items(1)
    logged_in_inventory.go_to_cart()
    
    cart = CartPage(page)
    cart.click_checkout()
    
    checkout = CheckoutPage(page)
    checkout.fill_information("", "", "")
    checkout.verify_error_msg("Error: First Name is required")
    