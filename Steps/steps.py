#!/usr/bin/env python3


def steps(points):
    for step in points:
        yield(step)

listofsteps = [100e3, 300e3, 1e6, 3e6, 10e6, 30e6, 50e6, 100e6, 300e6, 500e6, 1000e6, 1500e6, 2000e6, 2600e6, 3000e6, 4000e6, 4200e6]

numberofsteps = len(listofsteps)
print(numberofsteps)
print("")


stepper = steps(listofsteps)

step = next(stepper)  # First step
print(step)
print("")

step = next(stepper)  # Second step
print(step)
print("")


for step in stepper:  # Remaining steps
    print(step)
