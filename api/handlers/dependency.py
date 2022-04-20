from domain.registry import Registry

from ..repositories import (
    RoleRepository, PrefixRepository, UserRepository, DoctorRepository,
    PatientRepository, LogRepository, PatientListRepository
)

from database import CreatePostgresDb, SQLALCHEMY_DATABASE_URI


def inject():
    postgres_db = CreatePostgresDb(database_env=SQLALCHEMY_DATABASE_URI)

    Registry().role_repository = RoleRepository(next(postgres_db.get_db()))
    Registry().prefix_name_repository = PrefixRepository(next(postgres_db.get_db()))
    Registry().user_repository = UserRepository(next(postgres_db.get_db()))
    Registry().doctor_repository = DoctorRepository(next(postgres_db.get_db()))
    Registry().patient_repository = PatientRepository(next(postgres_db.get_db()))
    Registry().log_repository = LogRepository(next(postgres_db.get_db()))
    Registry().ptl_repository = PatientListRepository(next(postgres_db.get_db()))