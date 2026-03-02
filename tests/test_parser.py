import pytest


from shared import TEST_FILES

from settings import ENABLE_PARSER_TESTS


from app.parser import (
	parse_files,
	parse_report
)


pytestmark = pytest.mark.skipif(
	not ENABLE_PARSER_TESTS,
	reason='Tested'
)


def test_parse_files_success():
	try:
		list(
			parse_files(TEST_FILES)
		)
	except Exception as e:
		pytest.fail(str(e))


def test_parse_files_fail_wrong_extension():
	wrong_file = 'wrong_file.wrong'
	with pytest.raises(ValueError):
		list(
			parse_files([wrong_file])
		)


def test_parse_report_success():
	try:
		parse_report('average-gdp')
	except Exception as e:
		pytest.fail(str(e))


def test_parse_report_fail():
	with pytest.raises(SystemExit):
		parse_report('fail')
