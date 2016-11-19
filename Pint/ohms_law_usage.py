#!/usr/bin/env python3

from pint import UnitRegistry
import ohms_law as ohmslaw

ureg = UnitRegistry()


ret = ohmslaw.RVI(48 * ureg.volt, 0.96 * ureg.amp)
print(ret)
print(str(ret.magnitude) + " " + str(ret.units))

print(ohmslaw.VPR(50 * ureg.ohm, 6.432 * ureg.watt))  # 17.933209417167912 volt
print(ohmslaw.PVR(18 * ureg.volt, 50 * ureg.ohm))  # 6.48 watt
