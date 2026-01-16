import allure
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.account_page import AccountPage

scenarios('../features/login.feature')   

@given('que estou na página de login')
def open_login_page(login_page: LoginPage):
    with allure.step("Navegar para a página de login"):
        login_page.navigate()

@when(parsers.parse('eu preencho o email com "{email}"'))
def enter_email(login_page: LoginPage, email):
    with allure.step("Preencher o campo de email"):
        login_page.email_input.fill(email)

@when(parsers.parse('preencho a senha com "{password}"'))
def enter_password(login_page: LoginPage, password):
    with allure.step("Preencher o campo de senha"):
        login_page.password_input.fill(password)

@when('clico no botão de login')
def click_login(login_page: LoginPage):
    with allure.step("Clicar no botão de login"):
        login_page.login_button.click()

@then(parsers.parse('devo ser redirecionado para a área "{title_text}"'))
def verify_dashboard(account_page: AccountPage, title_text):
    with allure.step("Verificar redirecionamento para a área"):
        account_page.verify_login_success(title_text)

@then(parsers.parse('devo ver uma mensagem de erro "{message}"'))
def verify_error_message(login_page: LoginPage, message):
    with allure.step("Verificar mensagem de erro"):
        login_page.verify_login_error(message)

@then(parsers.parse('devo ver mensagens de erro "{message_email}" e "{message_password}"'))
def verify_required_fields_error(login_page: LoginPage, message_email, message_password):
    with allure.step("Verificar mensagens de erro para campos obrigatórios"):
        login_page.verify_email_required_error(message_email)
        login_page.verify_password_required_error(message_password)
