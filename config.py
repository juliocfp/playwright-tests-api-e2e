from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    env: str = "qa"

    base_url_dev: str 
    base_url_qa: str
    base_url_prd: str

    api_url_dev: str
    api_url_qa: str
    api_url_prd: str
    
settings = Settings()

def get_base_url(env_name: str) -> str:
    mapping = {
        "dev": settings.base_url_dev,
        "qa": settings.base_url_qa,
        "prd": settings.base_url_prd
    }
    return mapping.get(env_name.lower(), settings.base_url_qa)

def get_api_url(env_name: str) -> str:
    mapping = {
        "dev": settings.api_url_dev,
        "qa": settings.api_url_qa,
        "prd": settings.api_url_prd
    }
    return mapping.get(env_name.lower(), settings.api_url_qa)