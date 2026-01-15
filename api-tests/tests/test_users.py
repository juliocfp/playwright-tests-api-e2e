import pytest
from playwright.sync_api import APIRequestContext, expect

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
        
