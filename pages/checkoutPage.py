class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.checkout_button = "#checkout"
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.cart_link = ".shopping_cart_link"
        self.finish_button = "#finish"

    def go_to_cart(self):
        self.page.click(self.cart_link)

    def start_checkout(self):
        self.page.click(self.checkout_button)

    def fill_details(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.postal_code, postal_code)

    def continue_checkout(self):
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)