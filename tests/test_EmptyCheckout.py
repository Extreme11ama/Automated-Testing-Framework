from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage
from pages.checkoutPage import CheckoutPage

def test_checkout_empty_fields(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    cart = InventoryPage(page)
    cart.add_item("sauce-labs-backpack")

    checkout = CheckoutPage(page)
    checkout.go_to_cart()
    checkout.start_checkout()
    checkout.continue_checkout()

    error = page.locator("[data-test='error']").inner_text()

    assert "First Name is required" in error


def test_checkout_empty_cart(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    checkout = CheckoutPage(page)
    checkout.go_to_cart()
    checkout.start_checkout()
    checkout.continue_checkout()

    assert "checkout-step-one" in page.url