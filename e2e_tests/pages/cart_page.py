from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.nav_cart_button = page.locator("data-test=nav-cart")
        self.product_quantity_text = page.locator("data-test=product-quantity")
        self.proceed_button = page.locator("data-test=proceed-1")

    def navegate_to_cart(self):
        self.nav_cart_button.click()

    def verify_product_quantity(self, quantity):
        expect(self.product_quantity_text).to_be_visible()
        expect(self.product_quantity_text).to_have_value(quantity)

    def click_proceed(self):
        self.proceed_button.click()