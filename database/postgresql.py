import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


class CreatePostgresDb:
    def __init__(self, database_env):
        self.engine = _sql.create_engine(database_env)

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
