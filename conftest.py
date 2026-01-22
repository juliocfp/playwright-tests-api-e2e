import pytest
from config import get_base_url, get_api_url

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Ambiente de teste: dev, qa ou prd"
    )

@pytest.fixture(scope="session")
def current_env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(current_env):
    return get_base_url(current_env)

@pytest.fixture(scope="session")
def api_url(current_env):
    return get_api_url(current_env)