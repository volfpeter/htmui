from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        "env_file": ".env",
    }

    css_file: str = "basecoat.css"


settings = Settings()
