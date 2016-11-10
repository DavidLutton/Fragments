#!/usr/bin/env python3
from config import URLs
import pickler
from download import download

import feedparser
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

for URL in URLs:
    name, url, storename = URL
    print("####    " + name + "    ####")

    delta = storename + ".pickle"
    feed = feedparser.parse(url)

    entries = pickler.feeddelta(feed, delta)
    # pp(entries)

    if os.path.isdir(storename) is not True:
        print("  First run of " + name + " not downloading")
        print("  To download back catalog delete " + delta + " and run again")
        try:
            os.makedirs(storename)
        except OSError:
            pass
    else:
        # print(len(entries))
        for each in entries:
                for links in each.links:
                    if links['type'].startswith("audio/"):
                        try:
                            download(each.title, links['href'], storename)
                        except KeyError:
                            print("Paradox by Paradox")
    print()
