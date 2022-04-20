import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from database import PostgresqlConfig, CreatePostgresDb, SQLALCHEMY_DATABASE_URI


if SQLALCHEMY_DATABASE_URI is not None:
    _database = CreatePostgresDb(database_env=SQLALCHEMY_DATABASE_URI)
else:
    _database = CreatePostgresDb(config=PostgresqlConfig)


class Role(_database.Base):
    __tablename__ = "roles"
    role_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    role_nameth = _sql.Column(_sql.String, index=True, unique=True, nullable=True)
    role_nameen = _sql.Column(_sql.String, index=True, unique=True, nullable=False)
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)

    # One to Many
    users = _orm.relationship("User", backref="roles", cascade="all, delete")


class PrefixName(_database.Base):
    __tablename__ = "prefix_name"
    prefix_id = _sql.Column(_sql.VARCHAR(length=36), primary_key=True, index=True)
    prefix_nameth = _sql.Column(_sql.String, index=True, unique=True, nullable=False)
    prefix_nameen = _sql.Column(_sql.String, index=True, unique=True, nullable=True)
    prefix_ab_nameth = _sql.Column(_sql.String, index=True, unique=True, nullable=False)
    prefix_ab_nameen = _sql.Column(_sql.String, index=True, unique=True, nullable=True)
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)

    # One to Many
    users = _orm.relationship("User", backref="prefix_name", cascade="all, delete")


class User(_database.Base):
    __tablename__ = "users"
    user_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    email = _sql.Column(_sql.String, index=True, unique=True, nullable=False)
    password = _sql.Column(_sql.String, index=True, nullable=False)
    role_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("roles.role_id"))
    prefix_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("prefix_name.prefix_id"))
    first_name = _sql.Column(_sql.String, index=True, nullable=False)
    last_name = _sql.Column(_sql.String, index=True, nullable=False)
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)

    # One to One
    doctor = _orm.relationship("Doctor", back_populates="user", uselist=False, cascade="all, delete")
    patient = _orm.relationship("Patient", back_populates="user", uselist=False, cascade="all, delete")


class Doctor(_database.Base):
    __tablename__ = "doctors"
    doctor_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    doctor_code = _sql.Column(_sql.String, index=True, unique=True, nullable=False)
    user_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("users.user_id"))
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)

    # One to One
    user = _orm.relationship("User", back_populates="doctor", cascade="all, delete")

    # One to Many
    patients_list = _orm.relationship("PatientList", backref="doctor", cascade="all, delete")


class Patient(_database.Base):
    __tablename__ = "patients"
    pt_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    pt_code = _sql.Column(_sql.String, index=True, unique=True, nullable=False)
    user_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("users.user_id"))
    identity_number = _sql.Column(_sql.CHAR(13), index=True, unique=True, nullable=False)
    pt_birth_date = _sql.Column(_sql.DATE, index=True, nullable=True)
    pt_religion = _sql.Column(_sql.String, index=True, nullable=True)
    pt_address = _sql.Column(_sql.Text, index=True, nullable=True)
    pt_disease = _sql.Column(_sql.String, index=True, nullable=True)
    pt_weight = _sql.Column(_sql.Numeric(5, 2), index=True, nullable=True)
    pt_height = _sql.Column(_sql.Numeric(5, 2), index=True, nullable=True)
    pt_pressure = _sql.Column(_sql.Numeric(5, 2), index=True, nullable=True)
    pt_blood_type = _sql.Column(_sql.VARCHAR(25), index=True, nullable=True)
    pt_remark = _sql.Column(_sql.Text, index=True, nullable=True)
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)

    # 1 to 1
    user = _orm.relationship("User", back_populates="patient", cascade="all, delete")

    # One to Many
    apmts = _orm.relationship("Appointment", backref="patient", cascade="all, delete")
    estimate_logs = _orm.relationship("Log", backref="patient", cascade="all, delete")


class Appointment(_database.Base):
    __tablename__ = "appointment"
    apmt_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    pt_id = _sql.Column(_sql.String, _sql.ForeignKey("patients.pt_id"))
    apmt_datettime = _sql.Column(_sql.TIMESTAMP(timezone=True), index=True, nullable=True)
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)


class PatientList(_database.Base):
    __tablename__ = "patient_list"
    ptl_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    doctor_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("doctors.doctor_id"))
    pt_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("patients.pt_id"))


class Log(_database.Base):
    __tablename__ = "log"
    log_id = _sql.Column(_sql.VARCHAR(36), primary_key=True, index=True)
    doctor_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("doctors.doctor_id"))
    pt_id = _sql.Column(_sql.VARCHAR(36), _sql.ForeignKey("patients.pt_id"))
    log_level = _sql.Column(_sql.SMALLINT, index=True, nullable=False)
    log_desc = _sql.Column(_sql.Text, index=True, nullable=True)
    created_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)
    updated_at = _sql.Column(_sql.TIMESTAMP(timezone=True), nullable=True)