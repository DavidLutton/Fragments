from files import filetypeindir
from hashes import generate_hash

import os
import pprint

pprinter = pprint.PrettyPrinter(indent=4)
ppprint = pprinter.pprint


def deltachecksum(directory, filetype, trackingsubdir):
    filesNew = []
    filesChanged = []
    filesNoChange = []
    files = filetypeindir(directory, filetype)
    try:
        for filepath in files:

            track = trackingsubdir + os.sep + filepath + ".sha256"
            if os.path.isfile(track) is not True:
                with open(track, mode='w', encoding='utf-8') as obj:
                    obj.write(generate_hash(filepath))
                    filesNew.append(filepath)
            else:
                with open(track, mode='r', encoding='utf-8') as obj:
                    checksum = obj.read()
                    checksumnow = generate_hash(filepath)

                    if checksum == checksumnow:
                        pass
                        filesNoChange.append(filepath)
                    else:
                        filesChanged.append(filepath)

    except StopIteration:
        pass
    return(filesNoChange, filesNew, filesChanged)

filetype = ".pdf"
subdirfortrack = "Track"

if __name__ == "__main__":
    NoChange, New, Changed = deltachecksum(".", filetype, subdirfortrack)
    print("No change from initial checksum")
    ppprint(NoChange)
    print("New files, checksum saved")
    ppprint(New)
    print("Changed from first checksum")
    ppprint(Changed)
