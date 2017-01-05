#!/usr/bin/env python3

import pandas as pd


def parse(raw):

    points = []
    genlevel = []
    pwrlevel = []
    flag = False
    for line in raw.splitlines():
        if flag is False:
            if line == "{Data}":
                flag = True
        else:
            freq = line.split("\t")[0].strip()  # 0 colum of line seperated by \t
            genlvl = line.split("\t")[3].strip()  # 3 colum of line seperated by \t
            genlevel.append(genlvl)
            pwrlvl = float(line.split("\t")[4].strip())  # 4 colum of line seperated by \t

            freq, mul = freq.split(" ")
            # print(freq)
            dispatch = {
                "GHz": 1e9,
                "MHz": 1e6,
                "kHz": 1e3,
            }

            try:
                freq = float(freq) * dispatch[mul]
            except:
                raise NotImplementedError

            points.append(int(freq))
            # pwrlvl = 0
            pwrlvl = pwrlvl - ((-0.0000000024 * int(freq)) + 40.4)
            pwrlevel.append(pwrlvl)

    # print(points)
    # print(genlevel)
    # print(pwrlevel)
    # print(len(points))

    df = pd.DataFrame(
        {
            "Freq": points,
            "GenLevel": genlevel,
            "PwrLevel": pwrlevel
        },
    )
    return(df)
