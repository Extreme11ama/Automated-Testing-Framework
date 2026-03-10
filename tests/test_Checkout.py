from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage
from pages.checkoutPage import CheckoutPage

def test_checkout(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    cart = InventoryPage(page)
    cart.add_item("sauce-labs-backpack")

    checkout = CheckoutPage(page)
    checkout.go_to_cart()
    checkout.start_checkout()
    checkout.fill_details("test", "user", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "checkout-complete" in page.url