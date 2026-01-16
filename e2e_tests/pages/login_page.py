from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("data-test=email")
        self.password_input = page.locator("data-test=password")
        self.login_button = page.locator("data-test=login-submit")
        self.page_title = page.locator("h1") 
        self.error_alert = page.locator("data-test=login-error")

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/auth/login")

    def verify_login_success(self, text_title):
        expect(self.page_title).to_contain_text(text_title)

    def verify_login_error(self, message):
        expect(self.error_alert).to_be_visible()
        expect(self.error_alert).to_contain_text(message)
