import argparse


from app.reporter import cli_reporter

from app.constants import ALLOWED_EXTENSIONS_STR


def main():
	parser = argparse.ArgumentParser(
		description='''
		cli-utility for reading csv files
		'''
	)

	parser.add_argument(
		'--files', nargs='+', required=True,
		help=f'''
		List of files to create a report.
		Available file extensions: {ALLOWED_EXTENSIONS_STR}
		'''
	)

	parser.add_argument(
		'--report', required=True,
		help='''
		Most important argument. Must have value average-gdp.
		'''
	)

	cli_reporter(
		parser.parse_args()
	)


if __name__ == '__main__':
	main()
