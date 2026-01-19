from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.product_locator = page.locator("data-test=product")

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/")

    def select_product_by_name(self, product_name):
        product_locator = self.product_locator.filter(has_text=product_name)
        product_locator.click()