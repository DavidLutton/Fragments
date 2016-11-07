#!/usr/bin/env python3

from ETA import ETA

times = []

times.append(84.43)
times.append(21.231)

print(ETA(times, 48))
print("Time remaining {0} minutes".format(ETA(times, 48)))
