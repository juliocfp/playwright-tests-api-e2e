@web
Feature: Fluxo de compras
    Como um usuário do e-commerce
    Eu quero realizar uma compra com sucesso
    Para que eu possa receber meus produtos

    Background:
        Given que estou na página de detalhes do produto "Combination Pliers"

    Scenario Outline: Compra de um único produto
        When adiciono "<quantity>" unidade do produto ao carrinho
        And navego para o Checkout
        And realizo o login com as credenciais "customer2@practicesoftwaretesting.com" e "welcome01"
        And preencho o endereço de entrega
        And seleciono a forma de pagamento "Cash on Delivery"
        And finalizo a compra
        Then devo ver a mensagem de "Payment was successful"

        Examples:
            | quantity |
            | 1        |
            | 5        |
    
    Scenario Outline: Compra finalizada com <type>
        Given que estou na página de seleção do método de pagamento
        When seleciono a forma de pagamento "<type>"
        And preencho os detalhes do pagamento "<data>"
        And finalizo a compra
        Then devo ver a mensagem de "Payment was successful"

        Examples:
            | type              | data                                                                                                                |
            | Bank Transfer     | {"bank-name":"TEST BANK","account-name":"TEST TEST TEST","account-number":"010410851"}                              |
            | Cash on Delivery  | {}                                                                                                                  |
            | Credit Card       | {"credit-card-number":"4235-6477-2802-5682","expiration-date":"01/2050","cvv":"666","card-holder-name":"TEST TEST"} |
            | Buy Now Pay Later | {"installments":"3 Monthly Installments"}                                                                           |
            | Gift Card         | {"gift-card-number":"34534534","validation-code":"fgsd54"}                                                          |

    Scenario Outline: Tentativa de compra com Bank Transfer com dados inválidos
        Given que estou na página de seleção do método de pagamento
        When seleciono a forma de pagamento "Bank Transfer"
        And tento preencher com <scenario>
        Then devo ver a mensagem de erro <error>
        
        Examples:
            | scenario                | error                                                                                 |
            | Bank Name inválido      | Bank name can only contain letters and spaces.                                        |
            | Account Name inválido   | Account name can contain letters, numbers, spaces, periods, apostrophes, and hyphens. |
            | Account Number inválido | Account number must be numeric.                                                       |
            | vazio                   | todas                                                                                    |