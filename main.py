import uvicorn
import os
import sys

now_dir = os.getcwd()
sys.path.append(now_dir)

import config


def runDev():
    uvicorn.run(
        app="app:app",
        host=config.config["host"],
        port=config.config["port"],
        log_level="info",
        workers=1,
        reload=True,
        reload_dirs=[config.FRONTEND_PATH, "."],
        reload_includes=["*.py", "*.toml"],
        reload_delay=1,
    )


def runProd():
    uvicorn.run(
        app="app:app",
        host=config.config["host"],
        port=config.config["port"],
    )


def run():
    if config.config["mode"] == "development":
        runDev()
    else:
        runProd()


if __name__ == "__main__":
    run()
