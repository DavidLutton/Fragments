import os

from files import filetypeindir
from hashes import generate_hash

from deltasum import filetype

files = filetypeindir(".", filetype + ".track")

try:
    for filepath in files:
        os.remove(filepath)

except StopIteration:
    pass
