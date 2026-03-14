from argparse import ArgumentParser

from app.validators import validate_files

from app.constants import ALLOWED_EXTENSIONS_STR

from app.students.median_coffee_report import cli_median_coffee


REPORTS = {
    'median_coffee': cli_median_coffee
}


def main():
    parser = ArgumentParser(
        description='''
        cli-utility for processing csv-files.
        '''
    )

    parser.add_argument(
        '--report', 
        choices=list(REPORTS.keys()),
        required=True,
        type=str,
        help='''
        Report type.
        '''
    )
    
    parser.add_argument(
        '--files',
        required=True,
        nargs='+',
        help=f'''
        Files to work with. Allowed file extensions: {ALLOWED_EXTENSIONS_STR}
        '''
    )
    
    args = parser.parse_args()

    validate_files(args.files)

    REPORTS[args.report](args)


if __name__ == '__main__':
    main()
