@web
Feature: Login na Practice Software Testing
    Como um usuário registrado
    Quero acessar minha conta
    Para ver meus pedidos e dados

    Scenario: Login com credenciais válidas
        Given que estou na página de login
        When eu preencho o email com "customer@practicesoftwaretesting.com"
        And preencho a senha com "welcome01"
        And clico no botão de login
        Then devo ser redirecionado para a área "My account"

    Scenario: Tentativa de login com senha inválida
        Given que estou na página de login
        When eu preencho o email com "customer@practicesoftwaretesting.com"
        And preencho a senha com "senhaerrada123"
        And clico no botão de login
        Then devo ver uma mensagem de erro "Invalid email or password"
