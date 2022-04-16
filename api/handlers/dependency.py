from domain.registry import Registry
from ..repositories.role import RoleRepository
from database import PostgresqlConfig, CreatePostgresDb

def inject():
    postgres_db = CreatePostgresDb(PostgresqlConfig)
    Registry().role_repository = RoleRepository(next(postgres_db.get_db()))