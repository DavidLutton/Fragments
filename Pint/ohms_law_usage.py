#!/usr/bin/env python3

from pint import UnitRegistry
import ohms_law as ohmslaw

ureg = UnitRegistry()


ret = ohmslaw.RVI(48 * ureg.volt, 0.96 * ureg.amp)
print(ret)
print(str(ret.magnitude) + " " + str(ret.units))
