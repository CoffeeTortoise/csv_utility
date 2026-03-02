import pytest


from shared import run_command

from settings import ENABLE_CLI_TESTS


pytestmark = pytest.mark.skipif(
	not ENABLE_CLI_TESTS,
	reason='Tested'
)


def test_call_help_success():
	command = 'python -m main -h'
	_, err = run_command(command)
	assert not err


def test_call_fail_no_arguments():
	command = 'python -m main'
	_, err = run_command(command)
	assert err
