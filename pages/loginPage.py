class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"

    def load(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)

    def login_as_standard_user(self):
        self.login("standard_user", "secret_sauce")

    def login_as_locked_user(self):
        self.login("locked_out_user", "secret_sauce")
                             