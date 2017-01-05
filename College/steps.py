#!/usr/bin/env python3

import logging
from pprint import pprint
import pandas as pd

from stepsclass import FrequencySweep

import CIS9942.raw
import CIS9942.parse


# steps = [100e3, 300e3, 1e6, 3e6, 10e6, 30e6, 50e6, 100e6, 230e6]
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


log.info('Instance of FrequencySweep')
freq = FrequencySweep()
# freq.stepslist1centsteps(start=1e9, stop=6e9)
# freq.setpoints(sweep)
# freq.pointsofintrest()
# freq.sortbyfreq()

# freq.stepstrim(start=1e9, stop=1.4e9)
# pprint(freq.steps)
freq.stepslistpresetGHz()
print(freq.steps)
'''ste = FrequencyStepperinst.stepper()

point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
point = next(ste)
print(point)
FrequencyStepperinst.rewind = True

point = next(ste)
print(point)
for point in ste:
    print(point)
'''
df = CIS9942.parse.parse(CIS9942.raw.raw)
with pd.option_context('display.max_rows', 1024):
    print(df)

'''print(len(df))
# print(df.iloc[0])
freq, gen, pwr = df.iloc[0]
print(freq)
print(gen)
print(pwr)
# print(df.iloc[0][2])
'''
'''for frame in range(len(df)):
    freq, gen, pwr = df.iloc[frame]
    print(str(freq) + " " + str(gen) + " " + str(pwr))
'''
