class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"

    def loadSelf(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)