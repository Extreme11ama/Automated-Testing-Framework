def test_sort_products_az(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.select_option(".product_sort_container", "az")

    firstItem = page.locator(".inventory_item_name").first.inner_text()

    assert firstItem.startswith("Sauce Labs")

def test_sort_products_za(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.select_option(".product_sort_container", "za")

    first_item = page.locator(".inventory_item_name").first.inner_text()

    assert first_item != ""

def test_sort_price_low_high(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.select_option(".product_sort_container", "lohi")

    prices = page.locator(".inventory_item_price").all_inner_texts()

    prices = [float(p.replace("$", "")) for p in prices]

    assert prices == sorted(prices)

