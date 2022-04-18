from domain.registry import Registry

from ..repositories import (
    RoleRepository, PrefixRepository, UserRepository
)

from database import PostgresqlConfig, CreatePostgresDb, SQLALCHEMY_DATABASE_URI

def inject():
    if SQLALCHEMY_DATABASE_URI is not None:
        postgres_db = CreatePostgresDb(database_env=SQLALCHEMY_DATABASE_URI)
    else:
        postgres_db = CreatePostgresDb(config=PostgresqlConfig)
    Registry().role_repository = RoleRepository(next(postgres_db.get_db()))
    Registry().prefix_name_repository = PrefixRepository(next(postgres_db.get_db()))
    Registry().user_repository = UserRepository(next(postgres_db.get_db()))