import pytest


from settings import ENABLE_TABLER_TESTS

from factories import iter_random_avg_gdp


from app.tabler import (
	create_table,
	create_table_from_avg_gdp
)


pytestmark = pytest.mark.skipif(
	not ENABLE_TABLER_TESTS,
	reason='Tested'
)


def test_create_table_success():
	try:
		create_table(
			iterable=['1', '2', '3'],
			headers_=['4', '5', '6']
		)
	except Exception as e:
		pytest.fail(str(e))


def test_create_table_success_no_data():
	try:
		create_table(
			iterable=[],
			headers_=[]
		)
	except Exception as e:
		pytest.fail(str(e))


def test_create_table_fail_invalid_type():
	with pytest.raises(TypeError):
		create_table(
			iterable=['1', None, '3'],
			headers_=['4', '5', '6']
		)


def test_create_table_from_avg_gdp_success():
	avg_gdp = iter_random_avg_gdp(9)
	try:
		create_table_from_avg_gdp(avg_gdp)
	except Exception as e:
		pytest.fail(str(e))


def test_create_table_from_avg_gdp_success_no_data():
	try:
		create_table_from_avg_gdp([])
	except Exception as e:
		pytest.fail(str(e))


def test_create_table_from_avg_gdp_fail_invalid_type():
	avg_gdp = list(
		iter_random_avg_gdp(9)
	)
	avg_gdp.append(None)
	with pytest.raises(AttributeError):
		create_table_from_avg_gdp(avg_gdp)
