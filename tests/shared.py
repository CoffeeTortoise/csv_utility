import os

import sys

from subprocess import (
    Popen,
    PIPE
)


CWD = os.getcwd()

sys.path.append(CWD)


from app.constants import (
    ENCODING,
    ALLOWED_EXTENSIONS
)


TEST_FILES_FOLDER = os.path.join(CWD, 'tests', 'reports')

TEST_FILES: frozenset[str] = frozenset(
    os.path.join(TEST_FILES_FOLDER, file_)
    for file_
    in os.listdir(TEST_FILES_FOLDER)
    if file_.split(os.extsep)[-1] in ALLOWED_EXTENSIONS
)

INVALID_FILE = os.path.join(TEST_FILES_FOLDER, 'clown.png')

TEST_FILES_ARGS_STR = ' '.join(TEST_FILES)

ENABLE_FILE_SCHEME_TESTS = True

ENABLE_MEDIAN_COFFEE_REPORT_TESTS = True


def run_command(command: str) -> str:
    proc = Popen(
        command,
        shell=True,
        stdout=PIPE,
        stderr=PIPE
    )
    out, err = proc.communicate()
    return err.decode(ENCODING).strip()
