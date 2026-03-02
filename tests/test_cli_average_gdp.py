import pytest


from shared import (
	run_command,
	TEST_FILES_ARGS
)

from settings import ENABLE_CLI_AVERAGE_GDP_TESTS


pytestmark = pytest.mark.skipif(
	not ENABLE_CLI_AVERAGE_GDP_TESTS,
	reason='Tested'
)


def test_call_average_gdp_success():
	command = f'''
		python -m main --files {TEST_FILES_ARGS} --report average-gdp
	'''
	_, err = run_command(command)
	assert not err


def test_call_average_gdp_fail_wrong_report():
	command = f'''
		python -m main --files {TEST_FILES_ARGS} --report wrong_report
	'''
	_, err = run_command(command)
	assert 'Cannot continue' in err


def test_call_average_gdp_fail_missed_files():
	command = 'python -m main --report average-gdp'
	_, err = run_command(command)
	assert 'required: --files' in err


def test_call_average_gdp_fail_missed_report():
	command = f'''
		python -m main --files {TEST_FILES_ARGS}
	'''
	_, err = run_command(command)
	assert 'required: --report' in err
