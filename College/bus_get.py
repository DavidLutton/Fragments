#!/usr/bin/env python3
from pprint import pprint
import visa

import traceback
import sys

# visa.log_to_screen()

try:
    rm = visa.ResourceManager()
    # print(rmVISA.list_resources())
except OSError:
    try:
        print("Using SIM bus")
        rm = visa.ResourceManager('default.yaml@sim')
    except FileNotFoundError:
        print("File for SIM not found")


resources = rm.list_resources()
pool = {}
for resource in resources:
    inst = rm.open_resource(resource, read_termination='\n', write_termination='\r\n' if resource.startswith('ASRL') else '\n')
    try:
        IDN = inst.query("*IDN?")

    except visa.VisaIOError:  # This was found with print(dir(visa))
        traceback.print_exc(file=sys.stdout)
    finally:
        pool[resource] = [IDN, inst]
print(pool)


# print(pool['GPIB0::11::65535::INSTR'][1].query("*IDN?"))
# inst = rm['SIM'].open_resource('GPIB0::11::65535::INSTR')
# print(inst.query("*IDN?"))

CFCalibrationMeter = {
    100e3: 99.0,
    300e3: 99.0,
    1e6: 99.0,
    3e6: 99.0,
    10e6: 99.0,
    30e6: 99.0,
    50e6: 99.0,
    100e6: 99.0,
    300e6: 99.0,
    500e6: 99.0,
    1000e6: 99.0,
    1500e6: 99.0,
    2000e6: 99.0,
    2600e6: 99.0,
    3000e6: 99.0,
    4000e6: 99.0,
    4200e6: 99.0,
}
instr = {}
instr["MeterFeedback"] = pool['GPIB0::11::65535::INSTR'][1], pool['GPIB0::11::65535::INSTR'][0], None
instr["SignalGenerator"] = pool['GPIB0::8::65535::INSTR'][1], pool['GPIB0::8::65535::INSTR'][0], None
instr["MeterCalibration"] = pool['GPIB0::13::65535::INSTR'][1], pool['GPIB0::13::65535::INSTR'][0], CFCalibrationMeter


pprint(instr)
