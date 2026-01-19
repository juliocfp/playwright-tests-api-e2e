from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.nav_cart_button = page.locator("data-test=nav-cart")
        self.proceed_button = page.locator("data-test=proceed-1")

    def navegate_to_cart(self):
        self.nav_cart_button.click()
        self.proceed_button.click()
