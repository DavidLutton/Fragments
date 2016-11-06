#!/usr/bin/env python3

import numpy as np
from pint import UnitRegistry
from pint.unit import UnitDefinition
from pint.converters import Converter


class LogConverter(Converter):
    is_multiplicative = False

    def to_reference(self, value, inplace=False):
        return value

    def from_reference(self, value, inplace=False):
        return value

ureg = UnitRegistry()
ureg.default_format = '~P'
ureg.load_definitions('FrequencyRegistry.txt')

with ureg.context('rf'):
    Z = (ureg.ohm * 50)
    print(Z.magnitude)
    print(Z)
    print()

    q = (20 * ureg.cm)
    print(q.to('MHz'))

    q = (230 * ureg.MHz)
    print(q.to('cm'))

    print()
    print("6.432W")
    q = ((Z * (6.432 * ureg.watt)) ** .5)  # ** .5) == square root
    print(q)
    print(q.to('V'))

    print()
    print("18V")
    q = ((18 * ureg.volt) ** 2 / Z)
    print(q)
    print(q.to('W'))

    print()
    q = (13 * ureg.dBm) + (30 * ureg.dBm)
    print(q)
    print(q.to('dBm'))

    print()
    q = 20 * ureg.dBm
    print(q)
    print(q.magnitude)
    res = (10. ** ((q - 30)/10)) * ureg.watt
    print(res)

    print()
    q = 10 * ureg.watt
    print(q)
    print(q.magnitude)
    res = (10 * np.log10(q.magnitude / 0.001)) * ureg.dBm
    print(res)

    print()
    print("18V")
    q = ((18 * ureg.volt) ** 2 / Z).to('W')
    print(q)
    print(q.magnitude)
    res = (10 * np.log10(q.magnitude / 0.001)) * ureg.dBm
    print(res)
