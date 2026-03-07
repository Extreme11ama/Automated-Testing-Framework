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