import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext

load_dotenv()

@pytest.fixture(scope="session")
def api_gorest(playwright: Playwright) -> APIRequestContext:
    """
    Cria um contexto de API compartilhado para a sessão de testes.
    Define a URL base e headers padrões.
    """
    url = os.getenv("GOREST_BASE_URL")
    token = os.getenv("GOREST_TOKEN")
    
    request_context = playwright.request.new_context(
        base_url=url,
        extra_http_headers={
            "Authorization": token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )
    yield request_context
    request_context.dispose()
