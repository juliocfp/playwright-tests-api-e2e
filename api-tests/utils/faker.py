from faker import Faker

faker = Faker('pt_BR')

def get_user_payload():
    """Gera um payload de usuário com dados aleatórios válidos."""
    return {
        "name": faker.first_name(),
        "email": faker.email(),
        "gender": faker.random_element(elements=("male", "female")),
        "status": faker.random_element(elements=("active", "inactive"))
    }
