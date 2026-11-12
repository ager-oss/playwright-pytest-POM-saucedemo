from playwright.sync_api import Page, expect
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage

def test_TC_INV_05_navigate_to_detail_and_back(logged_in_inventory: InventoryPage, page: Page):
    """navigasi ke detail product lalu back"""
    product_name = "Sauce Labs Backpack"
    
    #Masuk ke detail product
    logged_in_inventory.click_product_name(product_name)
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    
    #kembali ke inventory
    page.click('[data-test="back-to-products"]')
    logged_in_inventory.verify_url("https://www.saucedemo.com/inventory.html")
    
def test_TC_INV_06_remove_item_directly_from_inventory(logged_in_inventory: InventoryPage):
    """tambah dan hapus product lgsg dari inventory page"""
    product_name = "Sauce Labs Backpack"
    
    #add to cart
    logged_in_inventory.add_item_by_name(product_name)
    logged_in_inventory.verify_cart_badge_count(1)
    
    #remove from inventory page
    logged_in_inventory.remove_item_by_name(product_name)
    logged_in_inventory.verify_cart_badge_count(0)