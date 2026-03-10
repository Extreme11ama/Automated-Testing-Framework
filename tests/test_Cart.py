from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage

def test_add_item_to_cart(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    cart = InventoryPage(page)
    cart.add_item("sauce-labs-backpack")

    assert cart.get_cart_count() == "1"

def test_remove_item_from_cart(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    cart = InventoryPage(page)
    cart.add_item("sauce-labs-backpack")
    assert cart.get_cart_count() == "1"

    cart.remove_item("sauce-labs-backpack")
    assert cart.get_cart_count() == "0"
