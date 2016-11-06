#!/usr/bin/env python3

import numpy as np
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.default_format = '~P'

print()
print("V=I*R")
qa = 20 * ureg.amp
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa * qb
print(res)
print(res.to(ureg.volt))

print()
print("V=P/I")
qa = 20 * ureg.watt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.volt))

print()
print("V=SQRT(P*R)")
qa = 20 * ureg.watt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = (qa * qb) ** .5
print(res)
print(res.to(ureg.volt))

print()
print("I=V/R")
qa = 20 * ureg.volt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.amp))

print()
print("I=SQRT(P/R)")
qa = 20 * ureg.watt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = (qa/qb) ** 0.5
print(res)
print(res.to(ureg.amp))

print()
print("I=P/V")
qa = 20 * ureg.watt
qb = 8 * ureg.volt
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.amp))

print()
print("P=V*I")
qa = 20 * ureg.volt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa * qb
print(res)
print(res.to(ureg.watt))

print()
print("P=I²*R")
qa = 20 * ureg.amp
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa ** 2 * qb
print(res)
print(res.to(ureg.watt))

print()
print("P=V²/R")
qa = 20 * ureg.volt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa ** 2 / qb
print(res)
print(res.to(ureg.watt))

print()
print("R=V²/P")
qa = 20 * ureg.volt
qb = 8 * ureg.watt
print(qa)
print(qb)
res = qa ** 2 / qb
print(res)
print(res.to(ureg.ohm))

print()
print("R=P/I²")
qa = 20 * ureg.watt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa / qb ** 2
print(res)
print(res.to(ureg.ohm))

print()
print("R=V/I")
qa = 20 * ureg.volt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.ohm))
