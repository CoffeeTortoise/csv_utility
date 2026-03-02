from itertools import chain

from collections import defaultdict


from .reader import read_csv

from .parser import (
	parse_files,
	parse_report
)

from .datatypes import AvgGDP

from .constants import TASK_PRECISION

from .tabler import create_table_from_avg_gdp


def get_iterable_avg(iterable, precision):
	avg = sum(iterable) / len(iterable)
	int_part_length = len(
		str(
			int(avg)
		)
	)
	precision += int_part_length
	return float(
		f'{avg: .{precision}}'
	)


def create_report(filepath):
	csv_data = list(
		read_csv(filepath)
	)
	grouped_data = defaultdict(list)
	for country_data in csv_data:
		grouped_data[country_data.country].append(
			country_data.gdp
		)
	for cntry, gdp in grouped_data.items():
		yield AvgGDP(
			country=cntry,
			avg_gdp=get_iterable_avg(
				gdp, TASK_PRECISION
			)
		)


def get_report(filepaths):
	return chain.from_iterable(
		create_report(filepath)
		for filepath
		in filepaths
	)


def sort_avg_gdp(avg_gdp):
	return sorted(
		avg_gdp,
		key=lambda i: i.avg_gdp,
		reverse=True
	)


def show_report(avg_gdp):
	print(
		create_table_from_avg_gdp(avg_gdp)
	)


def cli_reporter(parser_args):
	files = parse_files(parser_args.files)
	_ = parse_report(parser_args.report)
	show_report(
		sort_avg_gdp(
			get_report(files)
		)
	)
