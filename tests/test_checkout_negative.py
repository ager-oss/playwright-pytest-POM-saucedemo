import pytest
from playwright.sync_api import Page
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

@pytest.mark.parametrize("first_name, last_name, postal_code, expected_error", [
    ("Budi", "", "12345", "Error: Last Name is required"),
    ("Budi", "Santoso", "", "Error: Postal Code is required"),
    ("", "Santoso", "12345", "Error: First Name is required"),
])

def test_checkout_field_validation(logged_in_inventory: InventoryPage, page: Page, first_name, last_name, postal_code, expected_error):
    """TC-CHK-04, TC-CHK-05: Validasi form checkout secara parametrizing."""
    logged_in_inventory.add_first_n_items(1)
    logged_in_inventory.go_to_cart()
    
    cart = CartPage(page)
    cart.click_checkout()
    
    checkout = CheckoutPage(page)
    checkout.fill_information(first_name, last_name, postal_code)
    checkout.verify_error_msg(expected_error)
    
def test_TC_CHK_06_cancel_checkout_return_to_cart(logged_in_inventory: InventoryPage, page: Page):
    """TC-CHK-06: Pembatalan checkout mengembalikan user ke Cart."""
    logged_in_inventory.add_first_n_items(1)
    logged_in_inventory.go_to_cart()

    cart = CartPage(page)
    cart.click_checkout()

    checkout = CheckoutPage(page)
    checkout.click_cancel_on_info()

    cart.verify_url("https://www.saucedemo.com/cart.html")
    

    