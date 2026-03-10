from pages.loginPage import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    assert "inventory" in page.url

def test_login_failure(page):
    login = LoginPage(page)
    login.load()
    login.login_as_locked_user()

    error = page.locator("[data-test = 'error']").inner_text()

    assert "locked out" in error

def test_logout(page):
    login = LoginPage(page)
    login.load()
    login.login_as_standard_user()

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

    assert page.url == "https://www.saucedemo.com/"