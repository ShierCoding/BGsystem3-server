import os
import pathlib
from typing import Tuple


def Where() -> str:
    return os.path.normpath(os.path.dirname(os.path.abspath(__file__)))


def ToAbsolutePath(path: str) -> str:
    return os.path.normpath(os.path.abspath(os.path.join(Where(), path)))


def JoinPath(path: str, *paths: Tuple[str]) -> str:
    return os.path.normpath(os.path.join(path, *paths))


def ChangeSuffix(path: str, suffix: str) -> str:
    return pathlib.Path(path).with_suffix(suffix).__str__()
