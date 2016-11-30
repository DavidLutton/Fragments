import os


def filetypeindir(dir=None, filetype=None):
    """Yield a list of files in dir with given filetype."""
    for file in os.listdir(dir):
        if file.endswith(filetype):
            yield(file)
