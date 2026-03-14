from typing import (
    List,
    Iterable,
    Generator
)

from collections import (
    namedtuple,
    defaultdict
)

from statistics import median

from .file_scheme import FileScheme

from ..tabler import create_table


MedianCoffee = namedtuple(
    'MedianCoffee',
    [
        'student',
        'median_coffee'
    ]
)


def sort_median_coffee(median_coffee: Iterable[MedianCoffee], by_desc: bool) -> List[MedianCoffee]:
    return sorted(
        median_coffee,
        key=lambda student: student.median_coffee,
        reverse=by_desc
    )


def get_median_coffee_table(median_coffee: Iterable[MedianCoffee]) -> str:
    return create_table(
        (
            (student.student, student.median_coffee)
            for student
            in median_coffee
        ),
        headers_=['student', 'median_coffee']
    )


def get_median_coffee_per_student(filepaths: Iterable[str]) -> Generator[MedianCoffee]:
    student_coffee = defaultdict(list)
    for scheme in FileScheme.from_filepaths(filepaths):
        student_coffee[scheme.student].append(scheme.coffee_spent)
    for student, coffee_spents in student_coffee.items():
        yield MedianCoffee(
            student=student,
            median_coffee=median(coffee_spents)
        )


def cli_median_coffee(parser_args):
    files = parser_args.files
    median_coffee = get_median_coffee_per_student(files)
    sorted_median_coffee = sort_median_coffee(median_coffee, True)
    result_table = get_median_coffee_table(sorted_median_coffee)
    print(result_table)
