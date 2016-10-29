import numpy as np
from pint import UnitRegistry
ureg = UnitRegistry()
ureg.default_format = '~P'

# np.sqrt
# np.log10


def W2V(W, *, R=50):
    return(np.sqrt((R * ureg.ohm) * (W * ureg.watt)).to('V'))


def V2dBW(V, *, R=50):
    return(10. * np.log10(V * ureg.volt ** 2. / R * ureg.ohm))


def V2dBm(V, *, R=50):
    # return(10. * np.log10(V * ureg.volt ** 2. / R * ureg.ohm) + 30)
    return(10. * np.log10(V ** 2. / R) + 30)


def dBm2W(dBm):
    return((10. ** ((dBm - 30)/10)) * ureg.watt)


def dBW2W(dBm):
    return(10. ** (dBm / 10) * ureg.watt)


def W2dBm(W):
    return(10 * np.log10(W / 0.001))
    # return(10 * np.log10(W * ureg.watt / 0.001))


def W2dBW(W):
    # return(10 * np.log10(W))
    return(10 * np.log10(W))


def p(func, v):  # Present
    ret = func(v)
    print(func.__name__ + " " + str(v) + "  " + str(ret))
    return(ret)

for x in [-20, -10, 0, 3, 6, 10, 20, 30, 40, 50, 60, 70]:
    print()
    print(str(x) + " dBm")
    p(W2dBm, p(dBm2W, p(V2dBm, p(W2V, p(dBW2W, p(W2dBW, p(dBm2W, x).magnitude)).magnitude).magnitude)).magnitude)
