import databases
from urllib.parse import quote

from api.config import settings


POSTGRES_URL = f'postgresql://{settings.postgres_user}:{quote(settings.postgres_password)}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_database}'


postgres = databases.Database(POSTGRES_URL)
