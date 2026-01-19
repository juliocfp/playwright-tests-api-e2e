# 🌐 Camada de testes E2E

Módulo dedicado à simulação da jornada do usuário final nos navegadores (Chromium, Firefox, WebKit), validando fluxos visuais e interações.

## ⚙️ Configurações de Execução

Conforme definido na task `test-e2e` do projeto, os testes rodam com as seguintes configurações para facilitar o debug:

* **Headed:** O navegador é aberto visualmente na tela.
* **SlowMo (500ms):** Adiciona um atraso de meio segundo entre ações.
* **Tracing:** Grava vídeo e snapshots apenas se o teste falhar.

## 🏷️ Identificação (Markers)

Os testes localizados neste diretório devem ser identificados com a tag `@web` para serem reconhecidos pelos comandos globais.

## 🥒 BDD (Gherkin)

Este projeto utiliza **Pytest-BDD**. A estrutura recomendada é:

1.  **Features (`.feature`):** Arquivos de texto com a descrição do comportamento (Dado/Quando/Então).
2.  **Step Definitions:** Arquivos Python que traduzem os passos do Gherkin para código Playwright sem nenhuma lógica.
3.  **Page Object:** Arquivos Python com mapeamento dos elementos das páginas e ações realizadas.

## ▶️ Como Executar

A execução é centralizada na raiz do projeto via Taskipy.

* Para rodar apenas estes testes:
    `poetry run task test-e2e`

* Para rodar e ver o relatório:
    `poetry run task run-all-e2e`
