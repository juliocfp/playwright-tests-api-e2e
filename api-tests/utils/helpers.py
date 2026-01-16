from playwright.sync_api import APIRequestContext, APIResponse, expect
from utils.factories import get_user_payload

def create_user_helper(api_gorest: APIRequestContext) -> APIResponse:
    """Helper para criar um usuário e retornar o response."""
    response = api_gorest.post("/public/v2/users", data=get_user_payload())
    expect(response).to_be_ok()
    return response
