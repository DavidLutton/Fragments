#!/usr/bin/env python3
from config import URLs
import pickler
from download import download

import feedparser
import requests

import pprint
import pickle
import time
import os


def touch(fname, times=None):  # http://stackoverflow.com/a/1160227
    with open(fname, 'a'):
        os.utime(fname, times)

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

for URL in URLs:
    name, url, storename, mode = URL
    print("####    " + name + "    ####")

    # if os.path.isdir(storename) is not True:
    #    mode = 't'

    print(mode)
    delta = storename + ".pickle"
    feed = feedparser.parse(url)

    entries = pickler.feeddelta(feed, delta)

    print(len(entries))

    for each in entries:
            print("\n")
            for e in each:
                pass  # print(e)

            title = each.title

            for links in each.links:
                if links['type'].startswith("audio/"):
                    try:
                        download(title, links['href'], storename)
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

            '''
