from playwright.sync_api import Page, expect

class LoginCheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("data-test=email")
        self.password_input = page.locator("data-test=password")
        self.login_button = page.locator("data-test=login-submit")
        self.proceed_button = page.locator("data-test=proceed-2")

    def do_login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        self.proceed_button.click()