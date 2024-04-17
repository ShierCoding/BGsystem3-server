from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import config
import utils
import os
from transcode import main as transcode
import threading


app = FastAPI()


# 主页
@app.get("/", response_class=HTMLResponse)
async def main():
    return FileResponse(config.INDEX_PATH)


@app.get("/config/config.json")
async def read_item():
    return FileResponse(utils.JoinPath(config.CONFIG_PATH, config.DEFAULT_CONFIG))


@app.get("/open/timer")
async def exec():
    os.system(
        "start " + utils.ToAbsolutePath("../BGsystem3-timer/src-tauri/target/release/better-timer.exe"))
    return {"message": "success"}


app.mount("/config", StaticFiles(directory=config.CONFIG_PATH), name="config")


app.mount("/", StaticFiles(directory=config.FRONTEND_PATH), name="frontend")


threading.Thread(target=transcode).start()
