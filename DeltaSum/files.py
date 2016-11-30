import os


def filetypeindir(dir=None, filetype=None):
    """Generate a list of files in dir."""
    for file in os.listdir(dir):
        if file.endswith(filetype):
            yield(file)
