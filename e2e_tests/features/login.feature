@web
Feature: Login na Practice Software Testing
    Como um usuário registrado
    Quero acessar minha conta
    Para ver meus pedidos e dados

    Scenario: Login com credenciais válidas
        Given que estou na página de login
        When eu preencho o email com "customer3@practicesoftwaretesting.com"
        And preencho a senha com "pass123"
        And clico no botão de login
        Then devo ser redirecionado para a área "My account"

    Scenario: Tentativa de login com senha inválida
        Given que estou na página de login
        When eu preencho o email com "customer3@practicesoftwaretesting.com"
        And preencho a senha com "senhaerrada123"
        And clico no botão de login
        Then devo ver uma mensagem de erro "Invalid email or password"

    Scenario: Tentativa de login com email inválido
        Given que estou na página de login
        When eu preencho o email com "emailerrado@practicesoftwaretesting"
        And preencho a senha com "pass123"
        And clico no botão de login
        Then devo ver uma mensagem de erro "Invalid email or password"

    Scenario: Tentativa de login sem preencher campos
        Given que estou na página de login
        When clico no botão de login
        Then devo ver mensagens de erro "Email is required" e "Password is required"