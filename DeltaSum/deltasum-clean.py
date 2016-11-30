import os

from files import filetypeindir
from hashes import generate_hash


files = filetypeindir(".", ".pdf.track")

try:
    for filepath in files:
        os.remove(filepath)

except StopIteration:
    pass
