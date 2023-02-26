"""
Это основной мудуль
"""
import logging
import re
import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Any


def get_path(path: str) -> Path:
    """_summary_

    Args:
        path (str): путь получаемый из командной строки

    Returns:
        Path: путь преобразованный в Path
    """
    return Path(path)


class Parser:
    def __init__(self, path: Path, arg: tuple[str]) -> None:
        bs = BeautifulSoup()
        bs


def arg_worker() -> dict:
    """Обработчки аргументов командной строки

    Returns:
        Any: аргументы
    """
    args = argparse.ArgumentParser()
    return args


def main():
    pass


if __name__ == '__main__':
    main()
