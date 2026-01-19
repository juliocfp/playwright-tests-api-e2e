from playwright.sync_api import Page, expect

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.payment_list = page.locator("data-test=payment-method")
        self.bank_name_input = page.locator("data-test=bank-name")
        self.account_name_input = page.locator("data-test=account_name")
        self.account_number_input = page.locator("data-test=account_number")
        self.finish_button = page.locator("data-test=finish")
        self.expiration_date_input = page.locator("data-test=expiration_date")
        self.credit_card_name_input = page.locator("data-test=credit_card_name")
        self.cvv_input = page.locator("data-test=cvv")
        self.card_holder_name_input = page.locator("data-test=card_holder_name")
        self.monthly_installments_list = page.locator("data-test=monthly_installments")
        self.gift_card_number_input = page.locator("data-test=gift_card_number")
        self.validation_code_input = page.locator("data-test=validation_code")
        self.message_alert = page.locator("data-test=payment-success-message")

    def select_payment_method(self, method_name):
        self.payment_list.select_option(label=method_name)

    def fill_payment_details(self, method_name, **kwargs):
        method = {
            "Bank Transfer": self._fill_bank_transfer_details,
            "Credit Card": self._fill_credit_card_details,
            "Gift Card": self._fill_gift_card_details,
            "Buy Now, Pay Later": self._fill_monthly_installments,
            "Cash on Delivery": lambda: None
        }
        if method_name not in method:
            raise ValueError(f"Payment method '{method_name}' is not supported.")
        
        method[method_name](**kwargs)

    def _fill_bank_transfer_details(self, bank_name, account_name, account_number):
        self.bank_name_input.fill(bank_name)
        self.account_name_input.fill(account_name)
        self.account_number_input.fill(account_number)

    def _fill_credit_card_details(self, credit_card_name, expiration_date, cvv, card_holder_name, monthly_installments):
        self.credit_card_name_input.fill(credit_card_name)
        self.expiration_date_input.fill(expiration_date)
        self.cvv_input.fill(cvv)
        self.card_holder_name_input.fill(card_holder_name)

    def _fill_monthly_installments(self, monthly_installments):
        self.monthly_installments_list.select_option(label=monthly_installments)

    def _fill_gift_card_details(self, gift_card_number, validation_code):
        self.gift_card_number_input.fill(gift_card_number)
        self.validation_code_input.fill(validation_code)

    def click_finish(self):
        self.finish_button.click()
    
    def verify_confirmation_message(self, message):
        expect(self.message_alert).to_be_visible()
        expect(self.message_alert).to_contain_text(message)