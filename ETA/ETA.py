#!/usr/bin/env python3

import statistics


def ETA(ticktimes, ticksremaining):
    """
    [] of tick times
    int ticks remaining
    str return(minutes)"""
    return("{0:.1f}".format((statistics.mean(ticktimes) * ticksremaining) / 60))
