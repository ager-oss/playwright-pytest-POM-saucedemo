from playwright.sync_api import Page, expect
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage

def test_TC_CRT_06_cart_persistence_across_pages(logged_in_inventory: InventoryPage, page: Page):
    """memastikan keranjang tetap tersimpan"""
    added_items = logged_in_inventory.add_first_n_items(2)
    
    #pindah ke cart
    logged_in_inventory.go_to_cart()
    cart = CartPage(page)
    cart.verify_cart_items(added_items)
    