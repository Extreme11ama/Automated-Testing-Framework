def test_checkout(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("text=Add to cart")
    page.click(".shopping_cart_link")

    page.click("#checkout")

    page.fill("#first-name", "test")
    page.fill("#last-name", "user")
    page.fill("#postal-code", "12345")

    page.click("#continue")

    assert "checkout-step-two" in page.url