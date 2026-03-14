from itertools import chain

from typing import (
    Iterable,
    Generator
)

from dataclasses import dataclass

from .validators import (
    validate_exam,
    validate_date,
    validate_mood,
    validate_student,
    validate_study_hours,
    validate_sleep_hours,
    validate_coffee_spent
)

from ..reader import csv_reader


@dataclass(frozen=True)
class FileScheme:
    student: str
    date_: str
    coffee_spent: int
    sleep_hours: float
    study_hours: int
    mood: str
    exam: str
    
    
    @staticmethod
    def from_filepath(filepath: str) -> Generator[FileScheme]:
        with csv_reader(filepath) as reader:
            for i, row in enumerate(reader):
                if i < 1:
                    continue
                yield FileScheme(
                    student=row[0],
                    date_=row[1],
                    coffee_spent=int(row[2]),
                    sleep_hours=float(row[3]),
                    study_hours=int(row[4]),
                    mood=row[5],
                    exam=row[6]
                )
    
    @staticmethod
    def from_filepaths(filepaths: Iterable[str]) -> chain[FileScheme]:
        return chain.from_iterable(
            FileScheme.from_filepath(path)
            for path
            in filepaths
        )
    
    
    def __post_init__(self):
        validate_exam(self.exam)
        validate_date(self.date_)
        validate_mood(self.mood)
        validate_student(self.student)
        validate_study_hours(self.study_hours)
        validate_sleep_hours(self.sleep_hours)
        validate_coffee_spent(self.coffee_spent)
