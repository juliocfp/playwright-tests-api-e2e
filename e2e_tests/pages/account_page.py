from playwright.sync_api import Page, expect

class AccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_title = page.locator("h1")

    def verify_login_success(self, text_title):
        expect(self.account_title).to_contain_text(text_title)