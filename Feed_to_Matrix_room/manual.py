from auth import url, host, room, token

import pprint

from matrix_client.api import MatrixHttpApi
from matrix_client.api import MatrixRequestError

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

matrix = MatrixHttpApi(host, token=token)

try:
    # pp(matrix.get_room_state(room))
    msg = input("Message : ")
    print(msg)
    print(matrix.send_message(room, msg))

except MatrixRequestError as e:
    print(e)
    if e.code == 400:
        print("Room ID/Alias in the wrong format")
    else:
        print("Couldn't find room.")
