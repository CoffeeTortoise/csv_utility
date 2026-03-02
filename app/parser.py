import os


from .transformer import str_to_filepath

from .constants import (
	ALLOWED_EXTENSIONS,
	ALLOWED_EXTENSIONS_STR
)


def parse_files(files):
	for f in files:
		filepath = str_to_filepath(f)
		ext = filepath.split(os.extsep)[-1]
		if ext not in ALLOWED_EXTENSIONS:
			raise ValueError(
				f'''
				File extension {ext} not allowed.\n
				Allowed file extensions: {ALLOWED_EXTENSIONS_STR}
				'''
			)
		yield filepath


def parse_report(report):
	if report != 'average-gdp':
		raise SystemExit(
			'''
				Cannot continue.\n
				\'report\' argument must be equal to average-gdp
			'''
		)
	return report
