import os

from files import filetypeindir
from hashes import generate_hash

filetype = ".pdf"


def deltasum(directory, filetype):
    filesNew = []
    filesChanged = []
    FilesNoChange = []
    files = filetypeindir(directory, filetype)
    try:
        for filepath in files:
            # print(filepath)

            track = filepath + ".track"
            if os.path.isfile(track) is not True:
                with open(track, mode='w', encoding='utf-8') as obj:
                    obj.write(generate_hash(filepath))
                    filesNew.append(filepath)
            else:
                with open(track, mode='r', encoding='utf-8') as obj:
                    checksum = obj.read()
                    checksumnow = generate_hash(filepath)

                    # print(checksum)
                    # print(checksumnow)

                    if checksum == checksumnow:
                        pass
                        FilesNoChange.append(filepath)
                        # print(filepath + " has not changed")
                    else:
                        filesChanged.append(filepath)
                        print(filepath + " has     changed")

    except StopIteration:
        pass
    return(FilesNoChange, filesNew, filesChanged)


if __name__ == "__main__":
    NoChange, New, Changed = deltasum(".", filetype)
    print(NoChange)
    print(New)
    print(Changed)
