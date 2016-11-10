#!/usr/bin/env python3

import os
import requests


def download(title, url, storename):
    filename = url.split("/")
    filename = storename + os.sep + os.sep.join(filename[2:])
    leadingpath = filename.split(os.sep)
    leadingpath = (os.sep).join(leadingpath[:-1])

    if os.path.isdir(leadingpath) is not True:
        try:
            os.makedirs(leadingpath)
        except OSError:
            pass

    if os.path.isfile(filename) is not True:

        # if mode == 't':
        #    touch(filename)

        # if mode == 'd':
        print(title)
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as fd:
            chunk_size = 1024 ** 2
            for chunk in r.iter_content(chunk_size):
                print(".", end="", flush=True)
                fd.write(chunk)
