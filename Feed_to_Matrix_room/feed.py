from auth import url, host, room, token

import feedparser
import pprint
import pickle
import time
import os

from matrix_client.api import MatrixHttpApi
from matrix_client.api import MatrixRequestError

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

delta = 'entries.pickle'

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
                entries.remove(ent)

with open(delta, 'wb') as f:
    ents = []
    for entry in feed.entries:
        ents.append(entry)
    pickle.dump(ents, f, pickle.HIGHEST_PROTOCOL)

matrix = MatrixHttpApi(host, token=token)

try:
    # pp(matrix.get_room_state(room))
    for each in entries:
        msg = each.title + "  " + each.link
        print(msg)
        print(matrix.send_message(room, msg))
        time.sleep(30)
except MatrixRequestError as e:
    print(e)
    if e.code == 400:
        print("Room ID/Alias in the wrong format")
    else:
        print("Couldn't find room.")
