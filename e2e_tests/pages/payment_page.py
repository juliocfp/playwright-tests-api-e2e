from playwright.sync_api import Page, expect

class PaymentPage:

    ALERT_BANK_NAME_INVALID = "Bank name can only contain letters and spaces."
    ALERT_ACCOUNT_NAME_INVALID = "Account name can contain letters, numbers, spaces, periods, apostrophes, and hyphens."
    ALERT_ACCOUNT_NUMBER_INVALID = "Account number must be numeric."
    INVALID_BANK_NAME = "67576567"
    INVALID_ACCOUNT_NAME = "@@@ ###"
    INVALID_ACCOUNT_NUMBER = "abcde 12345"

    def __init__(self, page: Page):
        self.page = page
        self.payment_list = page.locator("data-test=payment-method")
        self.bank_name_input = page.locator("data-test=bank_name")
        self.account_name_input = page.locator("data-test=account_name")
        self.account_number_input = page.locator("data-test=account_number")
        self.finish_button = page.locator("data-test=finish")
        self.expiration_date_input = page.locator("data-test=expiration_date")
        self.credit_card_number_input = page.locator("data-test=credit_card_number")
        self.cvv_input = page.locator("data-test=cvv")
        self.card_holder_name_input = page.locator("data-test=card_holder_name")
        self.monthly_installments_list = page.locator("data-test=monthly_installments")
        self.gift_card_number_input = page.locator("data-test=gift_card_number")
        self.validation_code_input = page.locator("data-test=validation_code")
        self.message_alert = page.locator("data-test=payment-success-message")
        self.error_alert = page.locator(".alert-danger")

    def select_payment_method(self, method_name):
        self.payment_list.select_option(label=method_name)

    def fill_payment_details(self, method_name, data):
        if not data:
            return
        
        methods = {
            "Bank Transfer": self._fill_bank_transfer_details,
            "Credit Card": self._fill_credit_card_details,
            "Gift Card": self._fill_gift_card_details,
            "Buy Now Pay Later": self._fill_monthly_installments,
            "Cash on Delivery": lambda: None
        }
        if method_name not in methods:
            raise ValueError(f"Payment method '{method_name}' is not supported.")
        
        exec = methods[method_name]
        exec(data)

    def _fill_bank_transfer_details(self, data):
        self.bank_name_input.fill(data["bank-name"])
        self.account_name_input.fill(data["account-name"])
        self.account_number_input.fill(data["account-number"])

    def _fill_credit_card_details(self, data):
        self.credit_card_number_input.fill(data["credit-card-number"])
        self.expiration_date_input.fill(data["expiration-date"])
        self.cvv_input.fill(data["cvv"])
        self.card_holder_name_input.fill(data["card-holder-name"])

    def _fill_monthly_installments(self, data):
        self.monthly_installments_list.select_option(label=data["installments"])
    
    def _fill_gift_card_details(self, data):
        self.gift_card_number_input.fill(data["gift-card-number"])
        self.validation_code_input.fill(data["validation-code"])

    def click_finish(self):
        self.finish_button.click()
    
    def verify_confirmation_message(self, message):
        expect(self.message_alert).to_be_visible()
        expect(self.message_alert).to_contain_text(message)

    def verify_error_message(self, message):
        if message == "todas":
            expect(self.error_alert.filter(has_text=self.ALERT_BANK_NAME_INVALID)).to_be_visible()
            expect(self.error_alert.filter(has_text=self.ALERT_ACCOUNT_NAME_INVALID)).to_be_visible()
            expect(self.error_alert.filter(has_text=self.ALERT_ACCOUNT_NUMBER_INVALID)).to_be_visible()
            return

        expect(self.error_alert.filter(has_text=message)).to_be_visible()

    def fill_invalid_payment_details(self, data):
        fields = {
            "Bank Name":      self.bank_name_input,
            "Account Name":   self.account_name_input,
            "Account Number": self.account_number_input
        }

        if "vazio" in data:
            for element in fields.values():
                element.focus()
                element.blur()
            return

        invalids = {
            "Bank Name":      self.INVALID_BANK_NAME,
            "Account Name":   self.INVALID_ACCOUNT_NAME,
            "Account Number": self.INVALID_ACCOUNT_NUMBER
        }

        for key, invalid in invalids.items():
            if key in data:
                fields[key].fill(invalid)
                break