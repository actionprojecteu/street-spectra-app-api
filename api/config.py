from pydantic import BaseSettings


class Settings(BaseSettings):

    log_level: str = "logging.INFO"

    external_hostname: str = "*"

    postgres_user: str = "postgres_username"
    postgres_password: str = "postgres_password"
    postgres_host: str = "postgres_host"
    postgres_port: int = 5432
    postgres_database: str = "streetspectra"



settings = Settings()
