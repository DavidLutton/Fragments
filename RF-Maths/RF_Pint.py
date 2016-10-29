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


ureg.load_definitions('RFRegistry.txt')

with ureg.context('rf', impedence=50):
    q = (20 * ureg.cm)
    print(q.to('MHz'))

    q = (230 * ureg.MHz)
    print(q.to('cm'))

'''
    # Some of the wanted combinations
    # W V dBm
    q = (18 * ureg.volt)
    print(q.to('dBm'))

    q = (6 * ureg.watt)
    print(q.to('V'))

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
