from playwright.sync_api import Page, expect

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.quantity_input = page.locator("data-test=quantity")
        self.add_to_cart_button = page.locator("data-test=add-to-cart")
        self.message_alert = page.locator("id=toast-container")
        self.cart_quantity_text = page.locator("data-test=cart-quantity")

    def input_quantity(self, quantity):
        self.quantity_input.fill(quantity)

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def verify_add_to_cart_success(self, quantity):
        expect(self.message_alert).to_be_visible()
        expect(self.message_alert).to_contain_text("Product added to shopping cart.")
        expect(self.cart_quantity_text).to_be_visible()
        expect(self.cart_quantity_text).to_contain_text(quantity)