from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    token: str


def load_config() -> Config:
    env = Env()
    env.read_env()
    return Config(token=env("BOT_TOKEN"))
