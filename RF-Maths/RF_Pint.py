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
# ureg.default_format = '.3f'
ureg.load_definitions('FrequencyRegistry.txt')

with ureg.context('rf'):
    Z = (ureg.impedence * 50).to('ohm')
    print(Z.magnitude)
    print(Z)
    print()

    q = (20 * ureg.cm)
    print(q.to('MHz'))

    q = (230 * ureg.MHz)
    print(q.to('cm'))

    # Some of the wanted combinations W V dBm `/ 50Ω`
    print()
    q = ((Z * (6.432 * ureg.watt)) ** .5)
    # ** .5) == square root
    print(q)
    print(q.to('V'))

    print()
    q = (13 * ureg.dBm) + (30 * ureg.dBm)
    print(q)
    print(q.to('dBW'))

    print()
    '''q = (32 * ureg.dBW) + (30 * ureg.dBW)
    print(q)
    print(q.to('dBm'))
    '''
    '''print()
    q = (2 * ureg.dBW)
    print(q)
    '''

'''
    q = (18 * ureg.volt)
    print(q.to('dBm'))

    q = (32 * ureg.dBm)
    print(q.to('W'))

    q = (10 * ureg.watt)
    print(q.to('dBm'))

    # just an offset from dBm  30dB
    q = (18 * ureg.dBW)
    print(q.to('W'))

    q = (10 * ureg.watt)
    print(q.to('dBW'))

    q = (18 * ureg.volt)
    print(q.to('dBW'))
'''
