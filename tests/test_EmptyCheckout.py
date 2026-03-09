def test_checkout_empty_fields(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")

    page.click("#checkout")

    page.click("#continue")

    error = page.locator("[data-test='error']").inner_text()

    assert "First Name is required" in error


def test_checkout_empty_cart(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click(".shopping_cart_link")

    page.click("#checkout")

    assert "checkout-step-one" in page.url