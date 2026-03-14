import pytest

from shared import ENABLE_FILE_SCHEME_TESTS

from app.students.file_scheme import FileScheme


pytestmark = pytest.mark.skipif(
    not ENABLE_FILE_SCHEME_TESTS,
    reason='Not enabled'
)


@pytest.mark.parametrize(
    'student, date_, coffee_spent, sleep_hours, study_hours, mood, exam, error_class',
    [
        (11, '2024-06-06', 200, 7.5, 5, 'отл', 'Физика' , TypeError),
        ('Анна Белова', 14, 200, 7.5, 5, 'отл', 'Физика', TypeError),
        ('Анна Белова', '2024-06-06', '200', 7.5, 5, 'отл', 'Физика', TypeError),
        ('Анна Белова', '2024-06-06', -12, 7.5, 5, 'отл', 'Физика', ValueError),
        ('Анна Белова', '2024-06-06', 200, '7.5', 5, 'отл', 'Физика', TypeError),
        ('Анна Белова', '2024-06-06', 200, -7.5, 5, 'отл', 'Физика', ValueError),
        ('Анна Белова', '2024-06-06', 200, 7.5, '5', 'отл', 'Физика', TypeError),
        ('Анна Белова', '2024-06-06', 200, 7.5, -5, 'отл', 'Физика', ValueError),
        ('Анна Белова', '2024-06-06', 200, 7.5, 5, 0, 'Физика', TypeError),
        ('Анна Белова', '2024-06-06', 200, 7.5, 5, 'отл', 98, TypeError)
    ]
)
def test_create_file_scheme_fail(
    student: str,
    date_: str,
    coffee_spent: int,
    sleep_hours: float,
    study_hours: int,
    mood: str,
    exam: str,
    error_class: type
) -> None:
    with pytest.raises(error_class):
        FileScheme(
            student=student,
            date_=date_,
            coffee_spent=coffee_spent,
            sleep_hours=sleep_hours,
            study_hours=study_hours,
            mood=mood,
            exam=exam
        )


@pytest.mark.parametrize(
    'student, date_, coffee_spent, sleep_hours, study_hours, mood, exam',
    [
        ('Анна Белова', '2024-06-06', 200, 7.5, 5, 'отл', 'Физика')
    ]
)
def test_create_file_scheme_success(
    student: str,
    date_: str,
    coffee_spent: int,
    sleep_hours: float,
    study_hours: int,
    mood: str,
    exam: str
) -> None:
    try:
        FileScheme(
            student=student,
            date_=date_,
            coffee_spent=coffee_spent,
            sleep_hours=sleep_hours,
            study_hours=study_hours,
            mood=mood,
            exam=exam
        )
    except Exception as e:
        pytest.fail(str(e))
