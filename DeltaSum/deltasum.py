import os

from files import filetypeindir
from hashes import generate_hash


files = filetypeindir(".", ".pdf")
try:
    for filepath in files:
        # print(filepath)

        track = filepath + ".track"
        if os.path.isfile(track) is not True:
            with open(track, mode='w', encoding='utf-8') as obj:
                obj.write(generate_hash(filepath))
        else:
            with open(track, mode='r', encoding='utf-8') as obj:
                checksum = obj.read()
                checksumnow = generate_hash(filepath)

                # print(checksum)
                # print(checksumnow)

                if checksum == checksumnow:
                    pass
                    # print(filepath + " has not changed")
                else:
                    print(filepath + " has     changed")

except StopIteration:
    pass
