import pydantic

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):

    # model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="forbid")
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")


class UserConfig(BaseConfig):

    username: str
    password: str
