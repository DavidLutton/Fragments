#!/usr/bin/env python3
from config import URLs

import feedparser
import pprint
import pickle
import time
import os
import requests


def touch(fname, times=None):  # http://stackoverflow.com/a/1160227
    with open(fname, 'a'):
        os.utime(fname, times)

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

chunk_size = 1024 ** 2

for URL in URLs:
    name, url, shortname, mode = URL
    print("####    " + name + "    ####")

    # if os.path.isdir(shortname) is not True:
    #    mode = 't'
    print(mode)
    delta = shortname + ".pickle"
    feed = feedparser.parse(url)

    if os.path.isfile(delta) is not True:
        entries = []
        for entry in feed.entries:
            entries.append(entry)
    else:
        with open(delta, 'rb') as f:
            entries = []
            for entry in feed.entries:
                entries.append(entry)
            for ent in pickle.load(f):
                if ent in entries:
                    # pass
                    entries.remove(ent)

    with open(delta, 'wb') as f:
        ents = []
        for entry in feed.entries:
            ents.append(entry)
        pickle.dump(ents, f, pickle.HIGHEST_PROTOCOL)

    print(len(entries))

    for each in entries:
            print("\n")
            for e in each:
                pass  # print(e)

            print(each.title)

            for links in each.links:
                if links['type'].startswith("audio/"):
                    try:
                        print(links['href'])
                    except KeyError:
                        print("Paradox by Paradox")
            # print(each.guid)
            # for media in each.media_content:
            # print(each.title)
            # print(media.url)

            '''for media in each.media_content:
                if media['filesize'] is not '0':
                    print(each.title)
                    print(media['url'])

                    filename = media['url'].split("/")
                    filename = shortname + os.sep + os.sep.join(filename[2:])
                    leadingpath = filename.split(os.sep)
                    leadingpath = (os.sep).join(leadingpath[:-1])

                    if os.path.isdir(leadingpath) is not True:
                        try:
                            os.makedirs(leadingpath)
                        except OSError:
                            pass

                    if os.path.isfile(filename) is not True:

                        if mode == 't':
                            touch(filename)

                        if mode == 'd':
                            r = requests.get(media['url'], stream=True)
                            with open(filename, 'wb') as fd:
                                for chunk in r.iter_content(chunk_size):
                                    print(".", end="", flush=True)
                                    fd.write(chunk)
                '''
