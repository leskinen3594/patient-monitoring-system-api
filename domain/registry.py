from domain.base.singleton import Singleton


class Registry(metaclass=Singleton):
    def __init__(self):
        from domain.repositories.role import RoleRepositoryAbstract
        from domain.repositories.prefix_name import PrefixNameRepositoryAbstract
        from domain.repositories.user import UserRepositoryAbstract
        from domain.repositories.doctor import DoctorRepositoryAbstract
        from domain.repositories.patient import PatientRepositoryAbstract
        from domain.repositories.estimate_log import LogRepositoryAbstract
        from domain.repositories.patient_list import PatientListRepositoryAbstract
        from domain.repositories.appointment import AppointmentRepositoryAbstract

        self.role_repository: RoleRepositoryAbstract | None
        self.prefix_name_repository: PrefixNameRepositoryAbstract | None
        self.user_repository: UserRepositoryAbstract | None
        self.doctor_repository: DoctorRepositoryAbstract | None
        self.patient_repository: PatientRepositoryAbstract | None
        self.log_repository: LogRepositoryAbstract | None
        self.ptl_repository: PatientListRepositoryAbstract | None
        self.apmt_repository: AppointmentRepositoryAbstract | None