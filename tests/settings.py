import os

import sys

sys.path.append(os.curdir)


from app.constants import ENCODING as _ENCODING


TEST_DATA_DIR = os.path.join(
	os.curdir, 'tests', 'TestData'
)

ENCODING = _ENCODING

ENABLE_CLI_TESTS = True

ENABLE_PARSER_TESTS = True

ENABLE_READER_TESTS = True

ENABLE_TABLER_TESTS = True

ENABLE_REPORTER_TESTS = True

ENABLE_CLI_AVERAGE_GDP_TESTS = True
