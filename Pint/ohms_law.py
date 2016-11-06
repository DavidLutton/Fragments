#!/usr/bin/env python3

import numpy as np
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.default_format = '~P'

print()
qa = 20 * ureg.amp
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa * qb
print(res)
print(res.to(ureg.volt))

print()
qa = 20 * ureg.watt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.volt))

print()
qa = 20 * ureg.watt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = (qa * qb) ** .5
print(res)
print(res.to(ureg.volt))

print()
qa = 20 * ureg.volt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.amp))

print()
qa = 20 * ureg.watt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = (qa/qb) ** 0.5
print(res)
print(res.to(ureg.amp))

print()
qa = 20 * ureg.watt
qb = 8 * ureg.volt
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.amp))

print()
qa = 20 * ureg.volt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa * qb
print(res)
print(res.to(ureg.watt))

print()
qa = 20 * ureg.amp
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa ** 2 * qb
print(res)
print(res.to(ureg.watt))

print()
qa = 20 * ureg.volt
qb = 8 * ureg.ohm
print(qa)
print(qb)
res = qa ** 2 / qb
print(res)
print(res.to(ureg.watt))

print()
qa = 20 * ureg.volt
qb = 8 * ureg.watt
print(qa)
print(qb)
res = qa ** 2 / qb
print(res)
print(res.to(ureg.ohm))

print()
qa = 20 * ureg.watt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa / qb ** 2
print(res)
print(res.to(ureg.ohm))

print()
qa = 20 * ureg.volt
qb = 8 * ureg.amp
print(qa)
print(qb)
res = qa / qb
print(res)
print(res.to(ureg.ohm))
