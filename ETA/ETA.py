import statistics


def ETA(ticktimes, ticksremaining):
    return("{0:.1f}".format((statistics.mean(ticktimes) * ticksremaining) / 60))
