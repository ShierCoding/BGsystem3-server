import json
import os
import pathlib
from typing import List
import config
import utils
import ffmpy
from subprocess import PIPE


VIDEO_SUFFIX: List[str] = [".mp4", ".3gp", ".avi", ".wmv", ".mpeg",
                           ".mpg", ".mov", ".flv", ".swf", ".qsv",
                           ".kux", ".mpg", ".rm", ".ram"]


# 扫描config下所有视频，返回所有一个视频没有与其文件名相同的.webm文件的视频列表
def get_videos() -> List[str]:
    videos: List[str] = []

    for root, dirs, files in os.walk(config.CONFIG_PATH):
        for file in files:
            if pathlib.Path(file).suffix in VIDEO_SUFFIX:
                webm_file = utils.ChangeSuffix(file, '.webm')
                if webm_file not in files:
                    videos.append(file)

    return videos


# 读取json文件
def read_json():
    with open(config.CONFIG_JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


# 写入json文件
def write_json(data):
    with open(config.CONFIG_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 修改json文件内容
def modify_json():
    data = read_json()

    try:

        if data['style']['backgroundVideoSrc'] is not None:
            data['style']['backgroundVideoSrc'] = utils.ChangeSuffix(
                data['style']['backgroundVideoSrc'], ".webm")

        write_json(data)

    except:
        pass


# 视频转码
def transcode():
    videos = get_videos()

    for video in videos:
        input_path = utils.JoinPath(config.CONFIG_PATH, video)
        output_path = utils.ChangeSuffix(input_path, '.webm')

        ff = ffmpy.FFmpeg(
            inputs={input_path: None},
            outputs={output_path: "-c:v libvpx -crf 10 -b:v 0"},
            executable="../ffmpeg.exe"
        )

        print("$", ff.cmd)

        ff.run()


def main():
    modify_json()
    transcode()


if __name__ == "__main__":
    main()
