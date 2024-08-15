from pydantic_settings import BaseSettings


class PostgresConfig(BaseSettings):
    def uri(self):
        return f"postgresql://postgres:root@localhost:5432/time-ease-db"


postgresConfig = PostgresConfig()
