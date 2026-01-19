# 🔌 Camada de testes API

Módulo dedicado à validação de serviços backend, garantindo integridade de dados, contratos e regras de negócio sem a necessidade de interface gráfica.

## 🎯 Escopo dos Testes

* **Status Codes:** Validação de retornos HTTP (200, 201, 400, 401, etc.).
* **Contratos:** Validação da estrutura JSON das respostas.
* **Regras de Negócio:** Validação lógica dos dados processados.

## 🏷️ Identificação (Markers)

Os testes localizados neste diretório devem ser identificados com a tag `@api` (marker do Pytest) para serem reconhecidos pelos comandos globais.

## ▶️ Como Executar

A execução é centralizada na raiz do projeto via Taskipy.

* Para rodar apenas estes testes:
    `poetry run task test-api`

* Para rodar e ver o relatório:
    `poetry run task run-all-api`
