import os


import pytest


from shared import TEST_FILES

from settings import ENABLE_REPORTER_TESTS

from factories import iter_random_avg_gdp


from app.reporter import (
	show_report,
	get_iterable_avg,
	create_report,
	sort_avg_gdp
)


pytestmark = pytest.mark.skipif(
	not ENABLE_REPORTER_TESTS,
	reason='Tested'
)


def test_get_iterable_avg_success():
	gdp_list = 1.25, 1.55, 1.85
	precision = 1
	res = get_iterable_avg(
		gdp_list, precision
	)
	assert res == 1.6


def test_get_iterable_avg_success_integers():
	gdp_list = 3, 4, 5
	precision = 0
	res = get_iterable_avg(
		gdp_list, precision
	)
	assert res == 4


def test_get_iterable_avg_success_fail_invalid_type():
	with pytest.raises(TypeError):
		gdp_list = 3, 'tar', 4, 5
		get_iterable_avg(gdp_list, 0)


def test_create_report_success():
	try:
		rep = list(
			create_report(TEST_FILES[0])
		)
	except Exception as e:
		pytest.fail(str(e))
	else:
		assert rep is not None


def test_create_report_fail_file_does_not_exists():
	with pytest.raises(FileNotFoundError):
		list(
			create_report('file_not_exists.not')
		)


def test_create_report_fail_is_a_directory():
	with pytest.raises(IsADirectoryError):
		list(
			create_report(os.curdir)
		)


def test_sort_avg_gdp_success():
	avg_gdp = list(
		iter_random_avg_gdp(7)
	)
	try:
		sort_avg_gdp(avg_gdp)
	except Exception as e:
		pytest.fail(str(e))


def test_sort_avg_gdp_success_no_data():
	try:
		sort_avg_gdp([])
	except Exception as e:
		pytest.fail(str(e))


def test_sort_avg_gdp_fail_invalid_type():
	avg_gdp = list(
		iter_random_avg_gdp(3)
	)
	avg_gdp.append(None)
	with pytest.raises(AttributeError):
		sort_avg_gdp(avg_gdp)


def test_show_report_success():
	avg_gdp = iter_random_avg_gdp(9)
	try:
		show_report(avg_gdp)
	except Exception as e:
		pytest.fail(str(e))
