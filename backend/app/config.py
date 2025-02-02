from pydantic_settings import BaseSettings, SettingsConfigDict

class Env(BaseSettings):
  DEV_TEST_KEY: str
  OPENAI_API_KEY: str
  HUGGINGFACEHUB_API_TOKEN: str
  # Import env variables from .env file
  model_config = SettingsConfigDict(env_file=".env")

env = Env()