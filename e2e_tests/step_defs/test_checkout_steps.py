import allure
from e2e_tests.pages.address_page import AddressPage
from e2e_tests.pages.cart_page import CartPage
from e2e_tests.pages.login_checkout_page import LoginCheckoutPage
from e2e_tests.pages.payment_page import PaymentPage
from e2e_tests.pages.product_page import ProductPage
from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.account_page import AccountPage

scenarios('../features/checkout.feature')

@given(parsers.parse('que estou na página de detalhes do produto "{product_name}"'))
def open_product_page(home_page: HomePage, product_name: str):
    with allure.step("Navegar para a página inicial"):
        home_page.navigate()
    with allure.step(f"Selecionar o produto {product_name}"):
        home_page.select_product_by_name(product_name)

@when(parsers.parse('adiciono "{quantity}" unidade do produto ao carrinho'))
def add_product_to_cart(product_page: ProductPage, quantity: str):
    with allure.step(f"Adicionar {quantity} unidade do produto ao carrinho"):
        product_page.input_quantity(quantity)
        product_page.add_to_cart()
        
@when('navego para o Checkout')
def navigate_to_checkout(cart_page: CartPage):
    with allure.step("Navegar para o Checkout"):
        cart_page.navigate_to_checkout()

@when(parsers.parse('realizo o login com credenciais "{email}" e "{password}"'))
def login_with_valid_credentials(login_checkout_page: LoginCheckoutPage, email: str, password: str):
    with allure.step("Realizar login com credenciais válidas"):
        login_checkout_page.do_login(email, password)

@when('preencho o endereço de entrega')
def fill_delivery_address(address_page: AddressPage):
    with allure.step("Preencher o endereço de entrega"):
        address_page.fill_address()
        address_page.click_proceed()

@when(parsers.parse('seleciono a forma de pagamento "{payment_method}"'))
def select_payment_method(payment_page: PaymentPage, payment_method: str):
    with allure.step("Selecionar e preencher a forma de pagamento"):
        payment_page.select_payment_method(payment_method)
        payment_page.fill_payment_details(payment_method)

@when('finalizo a compra')
def finish_purchase(payment_page: PaymentPage): 
    with allure.step("Finalizar a compra"):
        payment_page.click_finish()

@then(parsers.parse('devo ver a mensagem de "{confirmation_message}"'))
def verify_confirmation_message(payment_page: PaymentPage, confirmation_message: str):
    with allure.step("Verificar a mensagem de confirmação"):
        payment_page.verify_confirmation_message(confirmation_message)