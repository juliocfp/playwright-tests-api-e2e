import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext

load_dotenv()

@pytest.fixture(scope="session")
def api_context(playwright: Playwright, api_url) -> APIRequestContext:
    """
    Cria um contexto de API compartilhado para a sessão de testes.
    Define a URL base e headers padrões.
    """ 
    token = os.getenv("API_TOKEN")
    
    request_context = playwright.request.new_context(
        base_url=api_url,
        extra_http_headers={
            "Authorization": token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )
    yield request_context
    request_context.dispose()
