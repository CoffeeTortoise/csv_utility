ENCODING: str = 'utf-8'

CSV_DELIMITER: str = ','

CSV_DIALECT: str = 'excel'

TABLE_FMT: str = 'pretty'

TABLE_ALIGN_COLUMN: str = 'left'

TASK_PRECISION: int = 2

ALLOWED_EXTENSIONS: frozenset[str] = frozenset(
	['csv']
)

ALLOWED_EXTENSIONS_STR: str = ', '.join(ALLOWED_EXTENSIONS)
