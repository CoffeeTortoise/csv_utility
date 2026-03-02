from tabulate import tabulate as tabled


from .constants import (
	TABLE_FMT,
	TABLE_ALIGN_COLUMN
)


def create_table(iterable, headers_):
	return tabled(
		iterable,
		headers=headers_,
		tablefmt=TABLE_FMT,
		stralign=TABLE_ALIGN_COLUMN
	)


def create_table_from_avg_gdp(avg_gdp):
	return create_table(
		(
			[ind, rdata.country, rdata.avg_gdp]
			for ind, rdata
			in enumerate(avg_gdp, start=1)
		),
		['#', 'country', 'gdp']
	)
