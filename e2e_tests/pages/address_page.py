from playwright.sync_api import Page, expect

class AddressPage:

    STREET = "Rua Nagib Tanus Gastin"
    CITY = "São Paulo"
    STATE = "SP"
    COUNTRY = "Brasil"
    POSTAL_CODE = "04173-170"

    def __init__(self, page: Page):
        self.page = page
        self.street_input = page.locator("data-test=street")
        self.city_input = page.locator("data-test=city")
        self.state_input = page.locator("data-test=state")
        self.country_input = page.locator("data-test=country")
        self.postal_code_input = page.locator("data-test=postal_code")
        self.proceed_button = page.locator("data-test=proceed-3")

    def fill_address(self):
        self.street_input.fill(self.STREET)
        self.city_input.fill(self.CITY)
        self.state_input.fill(self.STATE)
        self.country_input.fill(self.COUNTRY)
        self.postal_code_input.fill(self.POSTAL_CODE)

    def click_proceed(self):
        self.proceed_button.click()