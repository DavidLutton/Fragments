#!/usr/bin/env python3

import pickle
import os


def feeddelta(feed, deltafile):

    if os.path.isfile(deltafile) is not True:
        entries = []
        for entry in feed.entries:
            entries.append(entry)
    else:
        with open(deltafile, 'rb') as f:
            entries = []
            for entry in feed.entries:
                entries.append(entry)
            for ent in pickle.load(f):
                if ent in entries:
                    # pass
                    entries.remove(ent)

    with open(deltafile, 'wb') as f:
        ents = []
        for entry in feed.entries:
            ents.append(entry)
        pickle.dump(ents, f, pickle.HIGHEST_PROTOCOL)
    return(entries)
