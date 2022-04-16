from domain.base.singleton import Singleton


class Registry(metaclass=Singleton):
    def __init__(self):
        from domain.repositories.role import RoleRepositoryAbstract

        self.role_repository: RoleRepositoryAbstract | None