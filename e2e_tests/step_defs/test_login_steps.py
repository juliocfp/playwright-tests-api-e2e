from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/login.feature')   

@given('que estou na página de login')
def open_login_page(login_page: LoginPage):
    login_page.navigate()

@when(parsers.parse('eu preencho o email com "{email}"'))
def enter_email(login_page: LoginPage, email):
    login_page.email_input.fill(email)

@when(parsers.parse('preencho a senha com "{password}"'))
def enter_password(login_page: LoginPage, password):
    login_page.password_input.fill(password)

@when('clico no botão de login')
def click_login(login_page: LoginPage):
    login_page.login_button.click()

@then(parsers.parse('devo ser redirecionado para a área "{title_text}"'))
def verify_dashboard(login_page: LoginPage, title_text):
    login_page.verify_login_success(title_text)

@then(parsers.parse('devo ver uma mensagem de erro "{message}"'))
def verify_error_message(login_page: LoginPage, message):
    login_page.verify_login_error(message)
