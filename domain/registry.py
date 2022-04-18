from domain.base.singleton import Singleton


class Registry(metaclass=Singleton):
    def __init__(self):
        from domain.repositories.role import RoleRepositoryAbstract
        from domain.repositories.prefix_name import PrefixNameRepositoryAbstract

        self.role_repository: RoleRepositoryAbstract | None
        self.prefix_name_repository: PrefixNameRepositoryAbstract | None