import os


import pytest


from shared import TEST_FILES

from settings import ENABLE_READER_TESTS


from app.reader import read_csv


pytestmark = pytest.mark.skipif(
	not ENABLE_READER_TESTS,
	reason='Tested'
)


def test_read_csv_success():
	try:
		list(
			read_csv(f) for f
			in TEST_FILES
		)
	except Exception as e:
		pytest.fail(str(e))


def test_read_csv_fail_file_does_not_exists():
	file_ = 'not_existing_file.csv'
	with pytest.raises(FileNotFoundError):
		list(
			read_csv(file_)
		)


def test_read_csv_fail_is_a_directory():
	target = os.curdir
	with pytest.raises(IsADirectoryError):
		list(
			read_csv(target)
		)
