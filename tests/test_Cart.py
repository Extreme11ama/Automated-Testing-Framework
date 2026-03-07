def test_add_item_to_cart(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("text=Add to cart")

    cartBadge = page.locator(".shopping_cart_badge").inner_text()

    assert cartBadge == "1"

