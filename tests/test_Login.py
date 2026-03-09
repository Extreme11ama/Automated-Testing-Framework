from pages.loginPage import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.loadSelf()
    login.login("standard_user", "secret_sauce")

    assert "nventory" in page.url

def test_login_failure(page):
    login = LoginPage(page)
    login.loadSelf()
    login.login("locked_out_user", "secret_sauce")

    error = page.locator("[data-test = 'error']").inner_text()

    assert "locked out" in error

def test_logout(page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#react-burger-menu-btn")

    page.click("#logout_sidebar_link")

    assert "saucedemo.com" in page.url