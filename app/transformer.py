import os


def str_to_filepath(str_):
	return os.path.normpath(
		str_.strip()
	)
