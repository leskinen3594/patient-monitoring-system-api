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

from .estimate_log import (
    create_new_log, get_all_log, get_one_log,
    update_log_info, delete_log
)

from .patient_list import (
    create_new_ptl, get_all_ptl, get_one_ptl,
    update_ptl_info, delete_ptl
)

from .appointment import (
    create_new_apmt, get_all_apmt, get_one_apmt,
    update_apmt_info, delete_apmt, get_one_apmt_by_id
)