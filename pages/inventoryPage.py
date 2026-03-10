class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.cart_badge = ".shopping_cart_badge"

    def add_item(self, item_name):
        self.page.click(f"#add-to-cart-{item_name}")

    def remove_item(self, item_name):
        self.page.click(f"#remove-{item_name}")

    def get_cart_count(self):
        badge = self.page.locator(self.cart_badge)
        if badge.count() == 0:
            return "0"
        return badge.inner_text()