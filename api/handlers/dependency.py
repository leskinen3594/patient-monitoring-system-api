from domain.registry import Registry
from ..repositories.role import RoleRepository
from database import PostgresqlConfig, CreatePostgresDb, SQLALCHEMY_DATABASE_URI

def inject():
    if SQLALCHEMY_DATABASE_URI is not None:
        postgres_db = CreatePostgresDb(database_env=SQLALCHEMY_DATABASE_URI)
    else:
        postgres_db = CreatePostgresDb(config=PostgresqlConfig)
    Registry().role_repository = RoleRepository(next(postgres_db.get_db()))