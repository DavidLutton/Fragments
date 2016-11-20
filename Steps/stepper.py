#!/usr/bin/env python3


def steps(points):
    # print(points)
    for step in points:
        yield(step)


def test_steps():
    listofsteps = [100e3, 300e3, 1e6]
    # print(listofsteps)
    stepper = steps(listofsteps)
    assert next(stepper) == 100e3
    assert next(stepper) == 300e3
    assert next(stepper) == 1e6
