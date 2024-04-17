from typing import Final, TypedDict, NotRequired
import toml
import utils


class ConfigType(TypedDict):
    default: str
    host: str
    port: int
    mode: str


FRONTEND_PATH: Final = utils.ToAbsolutePath("../BGsystem3-frontend/dist/")
CURRENT_PATH: Final = utils.ToAbsolutePath(".")
INDEX_PATH: Final = utils.JoinPath(FRONTEND_PATH, "./index.html")
CONFIG_PATH: Final = utils.JoinPath(CURRENT_PATH, "./config/")
CONFIG_TOML_PATH: Final = utils.JoinPath(CURRENT_PATH, "./config.toml")


raw_config: ConfigType = toml.load(CONFIG_TOML_PATH)

default_config: ConfigType = {
    "default": "default.json",
    "host": "localhost",
    "port": 21233,
    "mode": "development",
}

for key in default_config:
    if key not in raw_config:
        raw_config[key] = default_config[key]

config: Final[ConfigType] = raw_config

DEFAULT_CONFIG: Final = config["default"]
CONFIG_JSON_PATH: Final = utils.JoinPath(CONFIG_PATH, DEFAULT_CONFIG)


print(f"当前路径:     {CURRENT_PATH}")
print(f"前端页面路径: {FRONTEND_PATH}")
print(f"前端主页路径: {INDEX_PATH}")
print(f"前端配置路径: {CONFIG_PATH}")
print(f"配置文件路径: {CONFIG_TOML_PATH}")
