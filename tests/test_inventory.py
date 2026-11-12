from pages.InventoryPage import InventoryPage

def test_TC_INV_01_sort_a_to_z(logged_in_inventory: InventoryPage):
    names = logged_in_inventory.get_all_product_names()
    assert names == sorted(names)
    
def test_TC_INV_02_sort_low_to_high(logged_in_inventory: InventoryPage):
    logged_in_inventory.sort_product("lohi")
    prices = logged_in_inventory.get_all_product_prices()
    assert prices == sorted(prices)
    
def test_TC_INV_03_sort_high_to_low(logged_in_inventory: InventoryPage):
    logged_in_inventory.sort_product("hilo")
    prices = logged_in_inventory.get_all_product_prices()
    assert prices == sorted(prices, reverse=True)
