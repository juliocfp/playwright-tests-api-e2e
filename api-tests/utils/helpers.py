from playwright.sync_api import APIRequestContext
from utils.faker import get_user_payload

def create_user_helper(api_gorest: APIRequestContext):
    """Helper para criar um usuário e retornar o response."""
    response = api_gorest.post("/public/v2/users", data=get_user_payload())
    assert response.ok
    return response
