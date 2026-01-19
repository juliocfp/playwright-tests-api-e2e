import json
import allure
from pages.address_page import AddressPage
from pages.cart_page import CartPage
from pages.login_checkout_page import LoginCheckoutPage
from pages.payment_page import PaymentPage
from pages.product_page import ProductPage
from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage

scenarios('../features/checkout.feature')

@given(parsers.parse('que estou na página de detalhes do produto "{product_name}"'))
def open_product_page(home_page: HomePage, product_name: str):
    with allure.step("Navegar para a página inicial"):
        home_page.navigate()
    with allure.step(f"Selecionar o produto {product_name}"):
        home_page.select_product_by_name(product_name)

@given('que estou na página de seleção do método de pagamento')
def open_payment_page(product_page: ProductPage, cart_page: CartPage, login_checkout_page: LoginCheckoutPage, address_page: AddressPage):
    quantity = "1"
    username = "customer2@practicesoftwaretesting.com"
    password = "welcome01"
    
    with allure.step("Navegar para a página de pagamento"):
        product_page.input_quantity(quantity)
        product_page.add_to_cart()
        product_page.verify_add_to_cart_success(quantity)
        cart_page.navegate_to_cart()
        cart_page.verify_product_quantity(quantity)
        cart_page.click_proceed()
        login_checkout_page.do_login(username, password)
        address_page.fill_address()
        address_page.click_proceed()

@when(parsers.parse('adiciono "{quantity}" unidade do produto ao carrinho'), target_fixture="quantity_added")
def add_product_to_cart(product_page: ProductPage, quantity: str):
    with allure.step(f"Adicionar {quantity} unidade do produto ao carrinho"):
        product_page.input_quantity(quantity)
        product_page.add_to_cart()
        product_page.verify_add_to_cart_success(quantity)

    return quantity
        
@when('navego para o Checkout')
def navigate_to_checkout(cart_page: CartPage, quantity_added: str):
    with allure.step("Navegar para o Checkout"):
        cart_page.navegate_to_cart()
    
    with allure.step("Verificar a quantidade de produto no carrinho"):
        cart_page.verify_product_quantity(quantity_added)

    with allure.step("Seguir para o Checkout"):
        cart_page.click_proceed()    

@when(parsers.parse('realizo o login com as credenciais "{email}" e "{password}"'))
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

@when(parsers.parse('seleciono a forma de pagamento "{payment_method}"'), target_fixture="selected_payment_method")
def select_payment_method(payment_page: PaymentPage, payment_method: str):
    with allure.step("Selecionar a forma de pagamento"):
        payment_page.select_payment_method(payment_method)

    return payment_method

@when(parsers.parse('preencho os detalhes do pagamento "{payment_data}"'))
def fill_payment_details(payment_page: PaymentPage, payment_data: str, selected_payment_method: str):
    with allure.step("Preencher os detalhes do pagamento"):
        data = json.loads(payment_data)

        if not data:
            return
        
        payment_page.fill_payment_details(selected_payment_method, data)

@when(parsers.parse('tento preencher com {payment_data}'))
def try_fill_invalid_payment_details(payment_page: PaymentPage, payment_data: str):
    with allure.step("Tentar preencher os detalhes do pagamento"):
        payment_page.fill_invalid_payment_details(payment_data)

@then(parsers.parse('devo ver a mensagem de "{confirmation_message}"'))
def verify_confirmation_message(payment_page: PaymentPage, confirmation_message: str):
    with allure.step("Verificar a mensagem de confirmação"):
        payment_page.verify_confirmation_message(confirmation_message)

@then(parsers.parse('devo ver a mensagem de erro {error_message}'))
def verify_error_message(payment_page: PaymentPage, error_message: str):
    with allure.step("Verificar a mensagem de erro"):
        payment_page.verify_error_message(error_message)