import os

from typing import Iterable

from argparse import ArgumentTypeError

from .constants import (
    ALLOWED_EXTENSIONS,
    ALLOWED_EXTENSIONS_STR
)


def validate_files(files: Iterable[str]) -> None:
    for f in files:
        if not os.path.isfile(f):
            raise ArgumentTypeError(
                f'File {f} does not exists!'
            )
        ext = f.split(os.extsep)[-1]
        if ext not in ALLOWED_EXTENSIONS:
            raise ArgumentTypeError(
                f'''
                File: {f}.\n
                File extension {ext} not allowed! Allowed extensions: {ALLOWED_EXTENSIONS_STR}.
                '''
            )
