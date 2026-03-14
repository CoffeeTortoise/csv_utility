from typing import (
	Any,
 	Iterable,
	Sequence
)

from tabulate import tabulate as tabled

from .constants import (
	TABLE_FMT,
	TABLE_ALIGN_COLUMN
)


def create_table(iterable: Iterable[Any], headers_: Sequence[str]) -> str:
	return tabled(
		iterable,
		headers=headers_,
		tablefmt=TABLE_FMT,
		stralign=TABLE_ALIGN_COLUMN
	)
