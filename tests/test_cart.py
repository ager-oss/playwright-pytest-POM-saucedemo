from playwright.sync_api import Page
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage

def test_TC_CRT_01_add_single_item(logged_in_inventory: InventoryPage):
    logged_in_inventory.add_item_by_name("Sauce Labs Backpack")
    logged_in_inventory.verify_cart_badge_count(1)

def test_TC_CRT_02_03_add_5_items_and_verify(logged_in_inventory: InventoryPage, page: Page):
    added_names = logged_in_inventory.add_first_n_items(5)
    logged_in_inventory.verify_cart_badge_count(5)
   
    logged_in_inventory.go_to_cart()
    cart = CartPage(page)
    cart.verify_cart_items(added_names)
    
def test_TC_CRT_05_add_all_items(logged_in_inventory: InventoryPage, page:Page):
    logged_in_inventory.add_first_n_items(3)
    logged_in_inventory.go_to_cart()
    
    cart = CartPage(page)
    cart.remove_all_items()
    cart.verify_cart_items([])
    
    cart = CartPage(page)
    cart.remove_all_items()
    cart.verify_cart_items([])
    logged_in_inventory.verify_cart_badge_count(0)
    

    
    