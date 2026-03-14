DATA_FORMAT: str = '%Y-%m-%d'

STRICT_VALIDATION: bool = False

EXAMS: frozenset[str] = frozenset(
    [
        'Программирование', 'Физика', 'Математика'
    ]
)

STUDENT_MOODS: frozenset[str] = frozenset(
    [
        'норм', 'устал', 'зомби', 
        'отл', 'не выжил', 'труп', 
        'легенда'
    ]
)
