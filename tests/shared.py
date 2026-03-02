import os

from subprocess import (
	Popen,
	PIPE
)


from settings import (
	ENCODING,
	TEST_DATA_DIR
)


TEST_FILES = list(
	os.path.join(TEST_DATA_DIR, f)
	for f in os.listdir(TEST_DATA_DIR)
)

TEST_FILES_ARGS = ' '.join(TEST_FILES)

COUNTRIES_LST = [
	'Denmark', 'China', 'Russia',
	'Finland', 'Spain', 'Turkey',
	'Switzerland', 'Indonesia',
	'South Korea', 'Italy', 'Brazil'
]


def run_command(command):
	proc = Popen(
		command,
		shell=True,
		stdout=PIPE,
		stderr=PIPE
	)
	out, err = proc.communicate()
	return (
		out.decode(ENCODING).strip(),
		err.decode(ENCODING).strip()
	)
