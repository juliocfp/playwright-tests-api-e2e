# 🎭 Automação de Testes (API & E2E)

Este repositório unifica a estratégia de testes automatizados de API e Interface (E2E) utilizando **Python**, **Playwright** e **Pytest**.

O projeto utiliza **Taskipy** para orquestrar os comandos, **Poetry** para gerenciamento de dependências e **Allure** para relatórios detalhados, além de suportar escrita de cenários em Gherkin com **Pytest-BDD**.

## 🛠️ Tecnologias

* **Python 3.11+**
* **Poetry** (Gerenciamento de dependências)
* **Playwright** (Engine de testes)
* **Pytest-BDD** (Escrita de cenários em Gherkin)
* **Allure Reports** (Relatórios de execução)

## 📂 Estrutura do Projeto
```text
/playwright-tests-api-e2e
├── /api-tests              # Diretório raiz dos testes de API (Backend)
│   ├── /tests              # Arquivos de especificação dos testes (test_*.py)
│   ├── /utils              # Funções utilitárias e helpers (ex: geradores de dados)
│   ├── conftest.py         # Configurações globais e Fixtures (setup/teardown) de API
│   └── README.md           # Documentação específica de execução da API
├── /e2e_tests              # Diretório raiz dos testes E2E (Frontend/UI)
│   ├── /features           # Arquivos de cenários em Gherkin (.feature)
│   ├── /pages              # Page Objects (Mapeamento de elementos e ações das telas)
│   ├── /step_defs          # Implementação técnica dos passos (Steps) do Gherkin
│   ├── conftest.py         # Configurações e Fixtures de Browser/Contexto para E2E
│   └── README.md           # Documentação específica de execução E2E
├── ./github                # Arquivo de configuração .yml da pipeline 
├── .env.example            # Modelo das variáveis de ambiente (template sem senhas reais)
├── poetry.lock             # Versões travadas das dependências (garantia de integridade)
├── config.py               # Gerenciamento centralizado de configurações (Pydantic Settings)
├── conftest.py             # Fixtures Globais (Seleção de ambiente --env, Hooks de Report)
├── pyproject.toml          # Configuração do projeto, dependências e scripts (Taskipy)
└── README.md               # Documentação principal (Instalação e Governança)
```
* `/api-tests`: Contém os testes de backend e validações de serviço.

* `/e2e_tests`: Contém os testes de interface, Page Objects e arquivos .feature (BDD).

## 🚀 Instalação e Configuração

1.  **Instalar Dependências:**
    Na raiz do projeto, execute o comando do Poetry para instalar as libs:

    `poetry install`

2.  **Instalar Navegadores:**
    Necessário para os testes de interface (E2E):

    `poetry run playwright install`

3.  **Configurar Variáveis de Ambiente:**
    O arquivo `.env.example` deve ser renomeado para `.env` e deve ser preenchido:
    
* com um token válido retirado de `https://gorest.co.in/my-account/access-tokens`

* com as URLs de cada ambiente: DEV, QA e PROD

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


