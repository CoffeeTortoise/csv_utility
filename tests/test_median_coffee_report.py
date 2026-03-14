import pytest

from shared import (
    run_command,
    INVALID_FILE,
    TEST_FILES_ARGS_STR,
    ENABLE_MEDIAN_COFFEE_REPORT_TESTS
)


REPORT_NAME: str = 'median_coffee'


pytestmark = pytest.mark.skipif(
    not ENABLE_MEDIAN_COFFEE_REPORT_TESTS,
    reason='Not enabled'
)


@pytest.mark.parametrize(
    'command, result',
    [
        (f'python -m main --files {TEST_FILES_ARGS_STR} --report wacky_report', 'invalid choice'),
        (f'python -m main --files {TEST_FILES_ARGS_STR}', 'required: --report'),
        (f'python -m main --files {TEST_FILES_ARGS_STR} --report', 'expected one'),
        (f'python -m main --files {TEST_FILES_ARGS_STR} wacky.csv --report {REPORT_NAME}', 'does not exists'),
        (f'python -m main --files --report {REPORT_NAME}', 'at least one'),
        (f'python -m main --files {TEST_FILES_ARGS_STR} {INVALID_FILE} --report {REPORT_NAME}', 'Allowed extensions:'),
        (f'python -m main --report {REPORT_NAME}', 'required: --files'),
        (f'python -m main', 'required: --report, --files')
    ]
)
def test_cli_median_coffee_fail(command: str, result: str) -> None:
    command_out = run_command(command)
    assert result in command_out or result == command_out


@pytest.mark.parametrize(
    'command, result',
    [
        (f'python -m main --files {TEST_FILES_ARGS_STR} --report {REPORT_NAME}', '')
    ]
)
def test_cli_median_coffee_success(command: str, result: str) -> None:
    command_out = run_command(command)
    assert result in command_out or result == command_out
