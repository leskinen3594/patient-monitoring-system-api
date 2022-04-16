from pydantic import BaseSettings
import yaml


class _ReadConfigFile:
    def __read_config_file(self) -> dict:
        # Input file or path/file
        file_name = 'configs/db.prod.yaml'

        with open(file_name) as file:
            self.content = yaml.safe_load(file)

        return self.content


class PostgresqlConfig(BaseSettings):
    __read_config = _ReadConfigFile()

    DRIVER: str = __read_config._ReadConfigFile__read_config_file()['driver']
    HOST: str = __read_config._ReadConfigFile__read_config_file()['host']
    PORT: str = __read_config._ReadConfigFile__read_config_file()['port']
    USER: str = __read_config._ReadConfigFile__read_config_file()['username']
    PASSWORD: str = __read_config._ReadConfigFile__read_config_file()['password']
    DATABASE: str = __read_config._ReadConfigFile__read_config_file()['database']
    SSL_MODE: str = __read_config._ReadConfigFile__read_config_file()['ssl_mode']
