import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

from .config import PostgresqlConfig


class CreatePostgresDb:
    def __init__(self, config: PostgresqlConfig):
        self.config = config()
        self.DATABASE_URL = f"{self.config.DRIVER}://{self.config.USER}:{self.config.PASSWORD}@{self.config.HOST}:{self.config.PORT}/{self.config.DATABASE}"

        if self.config.SSL_MODE:
            self.DATABASE_URL += f"?sslmode={self.config.SSL_MODE}"

        self.engine = _sql.create_engine(
                                            self.DATABASE_URL,
                                            pool_pre_ping=True,
                                            connect_args={
                                                "keepalives": 1,
                                                "keepalives_idle": 30,
                                                "keepalives_interval": 10,
                                                "keepalives_count": 5,
                                            })

        self.SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        self.Base =_declarative.declarative_base()


    def create_tables(self):
        return self.Base.metadata.create_all(bind=self.engine)


    def get_db(self):
        self.db = self.SessionLocal()
        try:
            yield self.db
        finally:
            self.db.close()


    # def close_db(self):
    #     self.db = self.SessionLocal()
    #     return self.db.close()