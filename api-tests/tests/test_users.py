import allure
from playwright.sync_api import APIRequestContext, expect
import pytest
from utils.factories import get_user_payload
from utils.helpers import create_user_helper

@pytest.mark.api
@allure.feature("API - Gestão de Usuários")
class TestUsersAPI:
    
    @allure.story("Listar Usuários")
    @allure.title("Deve listar todos os usuários com sucesso")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_users(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            create_user_helper(api_gorest)
        
        with allure.step("Requisição GET para listar usuários"):
            response = api_gorest.get("/public/v2/users")
        
        expect(response).to_be_ok()
        assert response.status == 200
        assert "application/json" in response.headers["content-type"]
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0, "A lista de usuários retornada está vazia."

        with allure.step("Validar contrato dos 5 primeiros usuários retornados"):
            for user in data[:5]:
                assert isinstance(user["id"], int)
                assert isinstance(user["name"], str)
                assert isinstance(user["email"], str)
                assert user["gender"] in ["male", "female"]
                assert user["status"] in ["active", "inactive"]

    @allure.story("Buscar Usuário")
    @allure.title("Deve buscar um usuário existente com sucesso")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            user_data = create_user_helper(api_gorest).json()
            user_id = user_data["id"]

        with allure.step("Requisição GET para buscar usuário específico"):
            response = api_gorest.get(f"/public/v2/users/{user_id}")
        
        expect(response).to_be_ok()
        assert response.status == 200
        assert "application/json" in response.headers["content-type"]
        
        data = response.json()       
        assert "id" in data

        with allure.step("Validar contrato do usuário retornado"):
            assert isinstance(data["id"], int)
            assert data["name"] == user_data["name"]
            assert data["email"] == user_data["email"]
            assert data["gender"] == user_data["gender"]
            assert data["status"] == user_data["status"]

    @allure.story("Buscar Usuário")
    @allure.title("Não deve retornar usuário inexistente")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_not_found(self, api_gorest: APIRequestContext):
        with allure.step("Requisição GET para usuário inexistente"):
            response = api_gorest.get("/public/v2/users/00000")
        
        assert response.status == 404
        data = response.json()

        with allure.step("Validar mensagem de erro para usuário inexistente"):
            assert data["message"] == "Resource not found"

    @allure.story("Criar Usuário")
    @allure.title("Deve criar um novo usuário com sucesso")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user(self, api_gorest: APIRequestContext): 
        payload = get_user_payload()

        with allure.step("Requisição POST para criar usuário"):
            response = api_gorest.post("/public/v2/users", data=payload)
        
        expect(response).to_be_ok()
        assert response.status == 201
        
        data = response.json()       
        assert "id" in data

        with allure.step("Validar contrato do usuário retornado"):
            assert isinstance(data["id"], int)
            assert data["name"] == payload["name"]
            assert data["email"] == payload["email"]
            assert data["gender"] == payload["gender"]
            assert data["status"] == payload["status"]

    @allure.story("Criar Usuário")
    @allure.title("Não deve criar usuário com email inválido")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_invalid_email(self, api_gorest: APIRequestContext):
        payload = get_user_payload()
        payload["email"] = "email_invalido"

        with allure.step("Requisição POST com email inválido"):
            response = api_gorest.post("/public/v2/users", data=payload)
        
        assert response.status == 422
        data = response.json()
        
        with allure.step("Validar mensagem de erro para email inválido"):
            assert isinstance(data, list)
            assert any(error["field"] == "email" and error["message"] == "is invalid" for error in data)

    @allure.story("Criar Usuário")
    @allure.title("Não deve criar usuário sem campos obrigatórios")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_missing_fields(self, api_gorest: APIRequestContext):
        with allure.step("Requisição POST sem campos obrigatórios"):
            response = api_gorest.post("/public/v2/users", data={})
        
        assert response.status == 422
        data = response.json()

        with allure.step("Validar mensagem de erro para campos em branco"):
            assert any(error["field"] == "name" and error["message"] == "can't be blank" for error in data)
            assert any(error["field"] == "email" and error["message"] == "can't be blank" for error in data)
            assert any(error["field"] == "gender" and error["message"] == "can't be blank, can be male of female" for error in data)
            assert any(error["field"] == "status" and error["message"] == "can't be blank" for error in data)

    @allure.story("Criar Usuário")
    @allure.title("Não deve criar usuário com JSON malformado")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_malformed_json(self, api_gorest: APIRequestContext):
        with allure.step("Requisição POST com JSON malformado"):
            response = api_gorest.post("/public/v2/users", data="{invalid_json")
        
        assert response.status == 401
        data = response.json()

        with allure.step("Validar mensagem de erro para JSON malformado"):
            assert data["message"] == "Authentication failed"

    @allure.story("Criar Usuário")
    @allure.title("Não deve criar usuário duplicado")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_duplicated_user(self, api_gorest: APIRequestContext):
        with allure.step("Requisição POST para criar primeiro usuário"):
            payload = get_user_payload()
            response = api_gorest.post("/public/v2/users", data=payload)
        
        expect(response).to_be_ok()
        assert response.status == 201
        
        with allure.step("Requisição POST para criar usuário duplicado"):
            response = api_gorest.post("/public/v2/users", data=payload)
        
        assert response.status == 422        
        data = response.json()       
        
        with allure.step("Validar mensagem de erro para usuário duplicado"):
            assert data[0]["field"] == "email"
            assert data[0]["message"] == "has already been taken"

    @allure.story("Criar Usuário")
    @allure.title("Não deve permitir criação sem autenticação")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_without_authentication(self, api_gorest: APIRequestContext):
        with allure.step("Requisição sem token válido"):
            response = api_gorest.post("/public/v2/users", headers={"Authorization": ""})
        
        assert response.status == 401
        data = response.json()

        with allure.step("Validar mensagem de erro para acesso não autorizado"):
            assert data["message"] == "Authentication failed"

    @allure.story("Atualizar Usuário")
    @allure.title("Deve atualizar um usuário existente")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            user_data = create_user_helper(api_gorest).json()
            user_id = user_data["id"]

        updated_payload = get_user_payload()

        with allure.step("Requisição PUT para atualizar usuário"):
            response = api_gorest.put(f"/public/v2/users/{user_id}", data=updated_payload)
        
        expect(response).to_be_ok()
        assert response.status == 200

        data = response.json()

        with allure.step("Validar contrato do usuário atualizado"):
            assert data["id"] == int(user_id)
            assert data["name"] == updated_payload["name"]

    @allure.story("Atualizar Usuário")
    @allure.title("Não deve atualizar usuário inexistente")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_not_found(self, api_gorest: APIRequestContext):
        payload = get_user_payload()
        
        with allure.step("Requisição PUT em usuário inexistente"):
            response = api_gorest.put("/public/v2/users/00000", data=payload)
        
        assert response.status == 404
        data = response.json()

        with allure.step("Validar mensagem de erro para usuário inexistente"):
            assert data["message"] == "Resource not found"

    @allure.story("Atualizar Usuário")
    @allure.title("Não deve permitir atualização sem autenticação")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_without_authentication(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            user_data = create_user_helper(api_gorest).json()
            user_id = user_data["id"]
        
        with allure.step("Requisição sem token válido"):
            response = api_gorest.put(f"/public/v2/users/{user_id}", headers={"Authorization": "Bearer token_invalido"})
        
        assert response.status == 401
        data = response.json()

        with allure.step("Validar mensagem de erro para acesso não autorizado"):
            assert data["message"] == "Invalid token"

    @allure.story("Remover Usuário")
    @allure.title("Deve remover um usuário existente")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            user_data = create_user_helper(api_gorest).json()
            user_id = user_data["id"]
        
        with allure.step("Requisição DELETE para remover usuário"):
            response = api_gorest.delete(f"/public/v2/users/{user_id}")
        
        expect(response).to_be_ok()
        assert response.status == 204
        
        with allure.step("Validar que o usuário foi removido"):
            assert response.text() == ""

    @allure.story("Remover Usuário")
    @allure.title("Não deve remover usuário inexistente")
    @allure.severity(allure.severity_level.MINOR)
    def test_delete_user_not_found(self, api_gorest: APIRequestContext):
        with allure.step("Requisição DELETE em usuário inexistente"):
            response = api_gorest.delete("/public/v2/users/00000")
        
        assert response.status == 404
        data = response.json()

        with allure.step("Validar mensagem de erro para usuário inexistente"):
            assert data["message"] == "Resource not found"

    @allure.story("Remover Usuário")
    @allure.title("Não deve permitir remoção sem autenticação")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user_without_authentication(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            user_data = create_user_helper(api_gorest).json()
            user_id = user_data["id"]
        
        with allure.step("Requisição sem token válido"):
            response = api_gorest.delete(f"/public/v2/users/{user_id}", headers={"Authorization": "Bearer token_invalido"})
        
        assert response.status == 401
        data = response.json()

        with allure.step("Validar mensagem de erro para acesso não autorizado"):
            assert data["message"] == "Invalid token"
