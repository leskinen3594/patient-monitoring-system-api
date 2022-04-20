from .role import (
    create_new_role, get_all_role, get_one_role,
    update_role_info, delete_role,
)

from .prefix_name import (
    create_new_prefix, get_all_prefix, get_one_prefix
)

from .user import (
    create_new_user, get_all_user, get_one_user,
    update_user_info, delete_user, login_user,
    login_doctor_detail, login_patient_detail
)

from .doctor import (
    create_new_doctor, get_all_doctor, get_one_doctor,
    update_doctor_info
)

from .patient import (
    create_new_patient, get_all_patient, get_one_patient,
    update_patient_info
)