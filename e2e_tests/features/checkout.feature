@web
Feature: Fluxo de compras
    Como um usuário do e-commerce
    Eu quero realizar uma compra com sucesso
    Para que eu possa receber meus produtos

    Background:
        Given que estou na página de detalhes do produto "Combination Pliers"

    Scenario: Compra de um único produto
        When adiciono "1" unidade do produto ao carrinho
        And navego para o Checkout
        And realizo o login com as credenciais "customer2@practicesoftwaretesting.com" e "welcome01"
        And preencho o endereço de entrega
        And seleciono a forma de pagamento "Credi Card"
        And finalizo a compra
        Then devo ver a mensagem de "Payment was successful"

