# 🎭 Automação de Testes (API & E2E)

Este repositório unifica a estratégia de testes automatizados de API e Interface (E2E) utilizando **Python**, **Playwright** e **Pytest**.

O projeto utiliza **Taskipy** para orquestrar os comandos, **Poetry** para gerenciamento de dependências e **Allure** para relatórios detalhados, além de suportar escrita de cenários em Gherkin com **Pytest-BDD**.

## 🛠️ Tecnologias

* **Python 3.11+**
* **Poetry** (Gerenciamento de dependências)
* **Playwright** (Engine de testes)
* **Pytest-BDD** (Escrita de cenários em Gherkin)
* **Allure Reports** (Relatórios de execução)

## 🚀 Instalação e Configuração

1.  **Instalar Dependências:**
    Na raiz do projeto, execute o comando do Poetry para instalar as libs:

    `poetry install`

3.  **Instalar Navegadores:**
    Necessário para os testes de interface (E2E):

    `poetry run playwright install`

## 🤖 Comandos de Execução (Tasks)

Utilize as *tasks* configuradas no arquivo `pyproject.toml` para executar os testes de forma padronizada.

### 🌐 Testes E2E (Interface)
Focados na jornada do usuário. Configurados para rodar com interface visual (`headed`), em câmera lenta e gerando traces em caso de falha.

* `poetry run task test-e2e`
    Executa apenas os testes marcados com a tag **@web**.

* `poetry run task run-all-e2e`
    Executa os testes E2E e gera o relatório Allure automaticamente ao final.

### 🔌 Testes de API (Backend)
Focados em contratos e regras de negócio no backend.

* `poetry run task test-api`
    Executa apenas os testes marcados com a tag **@api**.

* `poetry run task run-all-api`
    Executa os testes de API e gera o relatório Allure automaticamente ao final.

### 📊 Relatórios e Geral

* `poetry run task test-all`
    Executa **todos** os testes (API e E2E) de uma vez.

* `poetry run task report`
    Gera e abre o relatório HTML unificado (Allure) com os resultados da última execução.

## 📂 Estrutura do Projeto

* `/api-tests`: Contém os testes de backend e validações de serviço.
* `/e2e_tests`: Contém os testes de interface, Page Objects e arquivos .feature (BDD).
