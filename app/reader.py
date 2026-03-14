import csv

from contextlib import contextmanager

from .constants import (
	ENCODING,
	CSV_DIALECT,
	CSV_DELIMITER
)


@contextmanager
def csv_reader(filepath: str):
	with open(filepath, 'r', encoding=ENCODING) as f:
		reader = csv.reader(
			f,
			dialect=CSV_DIALECT,
			delimiter=CSV_DELIMITER
		)
		yield reader
