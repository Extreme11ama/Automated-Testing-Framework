def test_add_item_to_cart(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("text=Add to cart")

    cartBadge = page.locator(".shopping_cart_badge").inner_text()

    assert cartBadge == "1"

def test_remove_item_from_cart(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")

    cart_badge = page.locator(".shopping_cart_badge").inner_text()
    assert cart_badge == "1"

    page.click("#remove-sauce-labs-backpack")

    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.count() == 0
