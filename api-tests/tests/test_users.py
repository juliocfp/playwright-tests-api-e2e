import allure
from playwright.sync_api import APIRequestContext
from utils.factories import get_user_payload
from utils.helpers import create_user_helper

@allure.feature("Gestão de Usuários")
class TestUsersAPI:
    
    @allure.story("Listar Usuários")
    @allure.title("Deve listar todos os usuários com sucesso")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_users(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            create_user_helper(api_gorest)
        
        with allure.step("Requisição GET para listar usuários"):
            response = api_gorest.get("/public/v2/users")
        
        assert response.ok
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
        
    @allure.story("Criar Usuário")
    @allure.title("Deve criar um novo usuário com sucesso")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_user(self, api_gorest: APIRequestContext): 
        payload = get_user_payload()

        with allure.step("Requisição POST para criar usuário"):
            response = api_gorest.post("/public/v2/users", data=payload)
        
        assert response.ok
        assert response.status == 201
        
        data = response.json()       
        assert "id" in data

        with allure.step("Validar contrato do usuário retornado"):
            assert isinstance(data["id"], int)
            assert data["name"] == payload["name"]
            assert data["email"] == payload["email"]
            assert data["gender"] == payload["gender"]
            assert data["status"] == payload["status"]

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
        
        assert response.ok
        assert response.status == 200

        data = response.json()

        with allure.step("Validar contrato do usuário atualizado"):
            assert data["id"] == int(user_id)
            assert data["name"] == updated_payload["name"]

    @allure.story("Remover Usuário")
    @allure.title("Deve remover um usuário existente")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self, api_gorest: APIRequestContext):
        with allure.step("Pré-condição: Criar um usuário para garantir massa de dados"):
            user_data = create_user_helper(api_gorest).json()
            user_id = user_data["id"]
        
        with allure.step("Requisição DELETE para remover usuário"):
            response = api_gorest.delete(f"/public/v2/users/{user_id}")
        
        assert response.ok
        assert response.status == 204
        
        with allure.step("Validar que o usuário foi removido"):
            assert response.text() == ""
