import csv


from .datatypes import CountryData

from .constants import (
	ENCODING,
	CSV_DIALECT,
	CSV_DELIMITER
)


def read_csv(filepath):
	with open(filepath, 'r', encoding=ENCODING) as f:
		reader = csv.reader(
			f,
			dialect=CSV_DIALECT,
			delimiter=CSV_DELIMITER
		)
		for i, row in enumerate(reader):
			if i == 0:
				continue
			yield CountryData(
				country=row[0],
				year=int(row[1]),
				gdp=float(row[2]),
				gdp_growth=float(row[3]),
				inflation=float(row[4]),
				unemployment=float(row[5]),
				population=int(row[6]),
				continent=row[7]
			)
