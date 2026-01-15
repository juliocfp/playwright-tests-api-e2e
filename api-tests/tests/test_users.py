import pytest
from playwright.sync_api import APIRequestContext, expect
from utils.faker import get_user_payload

class TestUsersAPI:
    
    def test_get_all_users(self, api_gorest: APIRequestContext):
        """Valida a listagem de todos os usuários (GET)"""
        response = api_gorest.get("/public/v2/users")
        
        assert response.ok
        assert response.status == 200
        assert "application/json" in response.headers["content-type"]
        
        data = response.json()
        assert isinstance(data, list)
        
        assert "id" in data[0]
        assert "name" in data[0]
        assert "email" in data[0]
        assert "gender" in data[0]
        assert "status" in data[0]
        
    def test_create_user(self, api_gorest: APIRequestContext):
        """Valida a criação de um novo usuário (POST)"""
        response = create_user_helper(self, api_gorest)
        
        assert response.ok
        assert response.status == 201
        
        data = response.json()
       
        assert "id" in data
        assert isinstance(data["id"], int)

    def test_update_user(self, api_gorest: APIRequestContext):
        """Valida a atualização de um usuário (PUT)"""
        user_data = create_user_helper(self, api_gorest).json()
        user_id = user_data["id"]
        updated_payload = get_user_payload()
        updated_payload["username"] = "qa_updated"
        
        response = api_gorest.put(f"/public/v2/users/{user_id}", data=updated_payload)
        
        assert response.ok
        data = response.json()
        assert data["id"] == int(user_id)

    def test_delete_user(self, api_gorest: APIRequestContext):
        """Valida a remoção de um usuário (DELETE)"""
        user_data = create_user_helper(self, api_gorest).json()
        user_id = user_data["id"]
        
        response = api_gorest.delete(f"/public/v2/users/{user_id}")
        
        assert response.ok
        assert response.status == 204
        
        assert response.text() == ""

def create_user_helper(self, api_gorest: APIRequestContext):
    """Helper para criar um usuário e retornar o response."""
    response = api_gorest.post("/public/v2/users", data=get_user_payload())
    assert response.ok
    return response
