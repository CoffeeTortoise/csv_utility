from datetime import datetime

from .constants import (
    EXAMS,
    DATA_FORMAT,
    STUDENT_MOODS,
    STRICT_VALIDATION
)


def validate_student(student: str) -> None:
    if not isinstance(student, str):
        raise TypeError(
            'student field value should be string.'
        )


def validate_date(date_: str) -> None:
    if not isinstance(date_, str):
        raise TypeError(
            'date field value should be string.'
        )
    if not STRICT_VALIDATION:
        return
    try:
        datetime.strptime(date_, DATA_FORMAT)
        return
    except Exception:
        raise ValueError(
            f'Innapropriate data format. Should be: {DATA_FORMAT}.'
        )


def validate_coffee_spent(coffee_spent: int) -> None:
    if not isinstance(coffee_spent, int):
        raise TypeError(
            'coffee_spent field value should be int.'
        )
    if coffee_spent < 0:
        raise ValueError(
            'coffee_spent field value should be greater or equal to 0.'
        )


def validate_sleep_hours(sleep_hours: float) -> None:
    if STRICT_VALIDATION:
        if not isinstance(sleep_hours, float):
            raise TypeError(
                'sleep_hours field value should be float.'
            )
    else:
        if not isinstance(sleep_hours, (int, float)):
            TypeError(
                'sleep_hours field value should be either float or int.'
            )
    if sleep_hours < 0:
        raise ValueError(
            'sleep_hours field value should be greater or equal to 0.'
        )


def validate_study_hours(study_hours: int) -> None:
    if not isinstance(study_hours, int):
        raise TypeError(
            'study_hours field must be int.'
        )
    if study_hours < 0:
        raise ValueError(
            'study_hours field value should be greater or equal to 0.'
        )


def validate_mood(mood: str) -> None:
    if not isinstance(mood, str):
        raise TypeError(
            'mood field value should be string.'
        )
    if STRICT_VALIDATION:
        if mood not in STUDENT_MOODS:
            raise ValueError(
                f'Not allowed mood value: {mood}. Allowed: {', '.join(STUDENT_MOODS)}.'
            )


def validate_exam(exam: str) -> None:
    if not isinstance(exam, str):
        raise TypeError(
            'exam field value should be string.'
        )
    if STRICT_VALIDATION:
        if exam not in EXAMS:
            raise ValueError(
                f'Not allowed exam value: {exam}. Allowed: {', '.join(EXAMS)}.'
            )
