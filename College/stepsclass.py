#!/usr/bin/env python3
import logging


class FrequencySweep:

    def __init__(self):
        self.log = logging.getLogger(__name__)

        self.log.info('Instance of ' + __name__)
        self.rewind = False
        self.rewindDepth = -10
        self.steps = []

    def setpoints(self, steps):
        self.steps = steps
        self.stepslen = len(steps)

    def stepper(self):

        finished = False
        step = 0

        while not finished:

            yield self.steps[step]

            if self.rewind is True:
                self.rewind = False
                step += self.rewindDepth
                if step < 0:
                    step = 0
            else:
                step += 1

            if self.stepslen == step:
                finished = True

    def stepslist1centsteps(self, start=150e3, stop=230e6):

        listofsteps = []
        listofsteps.append(int(start))
        finished = False

        last = start
        while not finished:
            # print(listofsteps)
            last = last * 1.01
            listofsteps.append(int(last))
            if last > stop:
                listofsteps.remove(int(last))
                finished = True
        listofsteps.append(int(stop))
        # return(listofsteps)
        self.steps = listofsteps

    def stepslistpresetGHz(self):

        listofsteps = [
            1000000000, 1010000000, 1020000000, 1030000000, 1040999999, 1050999999, 1062000000, 1072000000, 1083000000,
            1094000000, 1105000000, 1116000000, 1127000000, 1138000000, 1149000000, 1161000000, 1173000000, 1184000000,
            1196000000, 1208000000, 1220000000, 1232000000, 1245000000, 1257000000, 1270000000, 1282000000, 1295000000,
            1308000000, 1321000000, 1335000000, 1348000000, 1361000000, 1375000000, 1389000000, 1403000000, 1417000000,
            1431000000, 1445000000, 1460000000, 1474000000, 1489000000, 1504000000, 1519000000, 1534000000, 1549000000,
            1565000000, 1580000000, 1596000000, 1612000000, 1628000000, 1645000000, 1661000000, 1678000000, 1694000000,
            1711000000, 1729000000, 1746000000, 1763000000, 1781000000, 1799000000, 1817000000, 1835000000, 1853000000,
            1872000000, 1890000000, 1909000000, 1928000000, 1948000000, 1967000000, 1987000000, 2007000000, 2027000000,
            2047000000, 2068000000, 2088000000, 2109000000, 2130000000, 2152000000, 2173000000, 2195000000, 2217000000,
            2239000000, 2261000000, 2284000000, 2307000000, 2330000000, 2353000000, 2377000000, 2400000000, 2424000000,
            2449000000, 2473000000, 2498000000, 2523000000, 2548000000, 2574000000, 2599000000, 2625000000, 2652000000,
            2678000000, 2705000000, 2732000000, 2759000000, 2787000000, 2815000000, 2843000000, 2871000000, 2900000000,
            2929000000, 2958000000, 2988000000, 3018000000, 3048000000, 3078000000, 3109000000, 3140000000, 3172000000,
            3203000000, 3235000000, 3268000000, 3300000000, 3333000000, 3367000000, 3400000000, 3434000000, 3469000000,
            3503000000, 3538000000, 3574000000, 3610000000, 3646000000, 3682000000, 3719000000, 3756000000, 3794000000,
            3832000000, 3870000000, 3909000000, 3948000000, 3987000000, 4027000000, 4067000000, 4107999999, 4149000000,
            4191000000, 4232999999, 4275000000, 4318000000, 4361000000, 4404000000, 4448000000, 4493000000, 4538000000,
            4583000000, 4629000000, 4675000000, 4722000000, 4769000000, 4817000000, 4865000000, 4914000000, 4963000000,
            5013000000, 5063000000, 5113000000, 5164000000, 5216000000, 5268000000, 5321000000, 5374000000, 5428000000,
            5482000000, 5537000000, 5592000000, 5648000000, 5705000000, 5762000000, 5819000000, 5878000000, 5936000000,
            5996000000, 6000000000]
        self.steps = listofsteps

    def stepslistpresetMHz(self):
        listofsteps = [
            80000000, 80800000, 81608000, 82424000, 83248000, 84081000, 84922000, 85771000, 86629000, 87495000,
            88370000, 89253000, 90146000, 91047000, 91958000, 92877000, 93806000, 94744000, 95692000, 96649000,
            97615000, 98591000, 99577000, 100573000, 101579000, 102595000, 103620000, 104657000, 105703000,
            106760000, 107828000, 108906000, 109995000, 111095000, 112206000, 113328000, 114461000, 115606000,
            116762000, 117930000, 119109000, 120300000, 121503000, 122718000, 123945000, 125185000, 126437000,
            127701000, 128978000, 130268000, 131570000, 132886000, 134215000, 135557000, 136913000, 138282000,
            139665000, 141061000, 142472000, 143897000, 145336000, 146789000, 148257000, 149739000, 151237000,
            152749000, 154277000, 155819000, 157378000, 158951000, 160541000, 162146000, 163768000, 165406000,
            167060000, 168730000, 170417000, 172122000, 173843000, 175581000, 177337000, 179110000, 180902000,
            182711000, 184538000, 186383000, 188247000, 190129000, 192031000, 193951000, 195890000, 197849000,
            199828000, 201826000, 203844000, 205883000, 207942000, 210021000, 212121000, 214242000, 216385000,
            218549000, 220734000, 222942000, 225171000, 227423000, 229697000, 231994000, 234314000, 236657000,
            239023000, 241414000, 243828000, 246266000, 248729000, 251216000, 253728000, 256266000, 258827999,
            261416000, 264031000, 266671000, 269338000, 272031000, 274751000, 277499000, 280274000, 283077000,
            285907000, 288766000, 291654000, 294571000, 297516000, 300491000, 303496000, 306531000, 309597000,
            312693000, 315819000, 318978000, 322167000, 325389000, 328643000, 331929000, 335249000, 338601000,
            341987000, 345407000, 348861000, 352350000, 355873000, 359432000, 363026000, 366656000, 370323000,
            374026000, 377767000, 381544000, 385360000, 389213000, 393105000, 397036000, 401007000, 405017000,
            409067000, 413158000, 417289000, 421462000, 425677000, 429934000, 434233000, 438575000, 442961000,
            447391000, 451864000, 456383000, 460947000, 465556000, 470212000, 474914000, 479663000, 484460000,
            489304000, 494197000, 499139000, 504131000, 509172000, 514264000, 519405999, 524600000, 529846000,
            535145000, 540496000, 545901000, 551360000, 556874000, 562443000, 568067000, 573748000, 579485000,
            585280000, 591133000, 597044000, 603015000, 609045000, 615135000, 621286000, 627499000, 633774000,
            640112000, 646513000, 652978000, 659508000, 666103000, 672764000, 679492000, 686287000, 693150000,
            700081000, 707082000, 714153000, 721294000, 728507000, 735792000, 743150000, 750582000, 758087000,
            765668000, 773325000, 781058000, 788869000, 796757000, 804725000, 812772000, 820900000, 829109000,
            837400000, 845774000, 854232000, 862774000, 871402000, 880116000, 888917000, 897806000, 906784000,
            915852000, 925010000, 934261000, 943603000, 953039000, 962570000, 972195000, 981917000, 991736000,
            1000000000]
        self.steps = listofsteps

    def stepslistpresetkHz(self):
        listofsteps = [
            150000, 151500, 153015, 154545, 156091, 157652, 159228, 160820, 162429, 164053, 165693, 167350,
            169024, 170714, 172421, 174145, 175887, 177646, 179422, 181216, 183028, 184859, 186707, 188574,
            190460, 192365, 194288, 196231, 198194, 200176, 202177, 204199, 206241, 208303, 210386, 212490,
            214615, 216761, 218929, 221118, 223329, 225563, 227818, 230097, 232398, 234722, 237069, 239439,
            241834, 244252, 246695, 249162, 251653, 254170, 256711, 259279, 261870, 264490, 267135, 269806,
            272504, 275229, 277982, 280761, 283569, 286405, 289269, 292162, 295083, 298034, 301014, 304024,
            307065, 310135, 313237, 316369, 319533, 322728, 325955, 329215, 332507, 335832, 339190, 342582,
            346008, 349468, 352963, 356493, 360058, 363658, 367295, 370968, 374677, 378424, 382208, 386030,
            389891, 393790, 397728, 401705, 405722, 409779, 413877, 418016, 422196, 426418, 430682, 434989,
            439339, 443732, 448169, 452651, 457177, 461749, 466367, 471030, 475741, 480498, 485303, 490156,
            495058, 500008, 505008, 510058, 515159, 520311, 525514, 530769, 536076, 541437, 546852, 552320,
            557843, 563422, 569056, 574746, 580494, 586299, 592162, 598083, 604064, 610105, 616206, 622368,
            628592, 634878, 641226, 647639, 654115, 660656, 667263, 673935, 680675, 687481, 694356, 701300,
            708313, 715396, 722550, 729775, 737073, 744444, 751888, 759407, 767001, 774671, 782418, 790242,
            798145, 806126, 814187, 822329, 830552, 838858, 847247, 855719, 864276, 872919, 881648, 890465,
            899369, 908363, 917447, 926621, 935887, 945246, 954698, 964245, 973888, 983627, 993463,
            1002999, 1012999, 1024000, 1034000, 1044000, 1055000, 1065000, 1076000, 1087000, 1097000, 1108000,
            1119000, 1131000, 1142000, 1153000, 1165000, 1177000, 1188000, 1200000, 1212000, 1224000, 1237000,
            1249000, 1261000, 1274000, 1287000, 1300000, 1313000, 1326000, 1339000, 1352000, 1366000, 1380000,
            1393000, 1407000, 1421000, 1436000, 1450000, 1464000, 1479000, 1494000, 1509000, 1524000, 1539000,
            1555000, 1570000, 1586000, 1602000, 1618000, 1634000, 1650000, 1667000, 1683000, 1700000, 1717000,
            1734000, 1752000, 1769000, 1787000, 1805000, 1823000, 1841000, 1860000, 1878000, 1897000, 1916000,
            1935000, 1954000, 1974000, 1994000, 2013999, 2033999, 2053999, 2075000, 2095000, 2116000, 2137000,
            2159000, 2180000, 2202000, 2224000, 2246000, 2269000, 2292000, 2315000, 2338000, 2361000, 2385000,
            2409000, 2433000, 2457000, 2482000, 2506000, 2531000, 2557000, 2582000, 2608000, 2634000, 2661000,
            2687000, 2714000, 2741000, 2769000, 2796000, 2824000, 2852000, 2881000, 2910000, 2939000, 2968000,
            2998000, 3028000, 3058000, 3089000, 3120000, 3151000, 3182000, 3214000, 3246000, 3279000, 3312000,
            3345000, 3378000, 3412000, 3446000, 3481000, 3515000, 3550000, 3586000, 3622000, 3658000, 3695000,
            3732000, 3769000, 3807000, 3845000, 3883000, 3922000, 3961000, 4001000, 4041000, 4081000, 4122000,
            4163000, 4205000, 4247000, 4289000, 4332000, 4376000, 4419000, 4464000, 4508000, 4553000, 4599000,
            4645000, 4691000, 4738000, 4786000, 4833000, 4882000, 4931000, 4980000, 5030000, 5080000, 5131000,
            5182000, 5234000, 5286000, 5339000, 5392000, 5446000, 5501000, 5556000, 5611000, 5667000, 5724000,
            5781000, 5839000, 5898000, 5957000, 6016000, 6076000, 6137000, 6198000, 6260000, 6323000, 6386000,
            6450000, 6515000, 6580000, 6646000, 6712000, 6779000, 6847000, 6915000, 6985000, 7054000, 7125000,
            7196000, 7268000, 7341000, 7414000, 7488000, 7563000, 7639000, 7715000, 7792000, 7870000, 7949000,
            8029000, 8109000, 8189999, 8272000, 8355000, 8438000, 8523000, 8608000, 8694000, 8781000, 8869000,
            8957000, 9047000, 9137000, 9229000, 9321000, 9414000, 9508000, 9603000, 9699000, 9796000, 9894000,
            9993000,
            10093000, 10194000, 10296000, 10399000, 10503000, 10608000, 10714000, 10821000, 10930000,
            11039000, 11149000, 11261000, 11373000, 11487000, 11602000, 11718000, 11835000, 11953000, 12073000,
            12194000, 12316000, 12439000, 12563000, 12689000, 12816000, 12944000, 13073000, 13204000, 13336000,
            13469000, 13604000, 13740000, 13878000, 14016000, 14157000, 14298000, 14441000, 14586000, 14731000,
            14879000, 15027000, 15178000, 15330000, 15483000, 15638000, 15794000, 15952000, 16111000, 16273000,
            16434999, 16600000, 16765999, 16933000, 17103000, 17274000, 17446000, 17621000, 17797000, 17975000,
            18155000, 18336000, 18520000, 18705000, 18892000, 19081000, 19272000, 19464000, 19659000, 19856000,
            20054000, 20255000, 20457000, 20662000, 20868000, 21077000, 21288000, 21501000, 21716000, 21933000,
            22152000, 22374000, 22598000, 22824000, 23052000, 23282000, 23515000, 23750000, 23988000, 24228000,
            24470000, 24715000, 24962000, 25211000, 25463000, 25718000, 25975000, 26235000, 26497000, 26762000,
            27030000, 27300000, 27573000, 27849000, 28128000, 28409000, 28693000, 28980000, 29270000, 29562000,
            29858000, 30157000, 30458000, 30763000, 31070000, 31381000, 31695000, 32012000, 32332000, 32655000,
            32982000, 33311999, 33645000, 33981000, 34321000, 34664000, 35011000, 35361000, 35714000, 36072000,
            36432000, 36797000, 37165000, 37536000, 37912000, 38291000, 38674000, 39060000, 39451000, 39846000,
            40244000, 40646000, 41053000, 41463000, 41878000, 42297000, 42720000, 43147000, 43578000, 44014000,
            44454000, 44899000, 45348000, 45801000, 46259000, 46722000, 47189000, 47661000, 48138000, 48619000,
            49105000, 49596000, 50092000, 50593000, 51099000, 51610000, 52126000, 52648000, 53174000, 53706000,
            54243000, 54785000, 55333000, 55886000, 56445000, 57010000, 57580000, 58156000, 58737000, 59325000,
            59918000, 60517000, 61122000, 61733000, 62351000, 62974000, 63604000, 64239999, 64882000, 65531000,
            66187000, 66848000, 67517000, 68192000, 68874000, 69563000, 70258000, 70961000, 71670000, 72387000,
            73111000, 73842000, 74581000, 75326000, 76080000, 76840000, 77609000, 78385000, 79169000, 79961000,
            80760000, 81568000, 82383000, 83207000, 84039000, 84880000, 85728000, 86586000, 87452000, 88326000,
            89209000, 90102000, 91003000, 91913000, 92832000, 93760000, 94698000, 95645000, 96601000, 97567000,
            98543000, 99528000,
            100523000, 101529000, 102544000, 103569000, 104605000, 105651000, 106708000, 107775000, 108852000,
            109941000, 111040000, 112151000, 113272000, 114405000, 115549000, 116705000, 117872000, 119050000,
            120241000, 121443000, 122658000, 123884000, 125123000, 126374000, 127638000, 128913999, 130204000,
            131506000, 132821000, 134149000, 135490000, 136845000, 138214000, 139596000, 140992000, 142402000,
            143826000, 145264000, 146717000, 148184000, 149666000, 151162000, 152674000, 154201000, 155743000,
            157300000, 158873000, 160462000, 162066000, 163687000, 165324000, 166977000, 168647000, 170333000,
            172037000, 173757000, 175495000, 177250000, 179022000, 180812000, 182620000, 184447000, 186291000,
            188154000, 190036000, 191936000, 193855000, 195794000, 197752000, 199729000, 201727000, 203744000,
            205781000, 207839000, 209917000, 212017000, 214137000, 216278000, 218441000, 220625000, 222832000,
            225060000, 227310000, 229584000, 230000000]
        self.steps = listofsteps

    def stepstrim(self, start=False, stop=False):
        trimmed = []

        if start is False:
            start = min(self.steps)
        if stop is False:
            stop = max(self.steps)

        for step in self.steps:
            if step >= start:
                if step <= stop:
                    trimmed.append(step)

        # return(trimmed)
        self.steps = trimmed

    def pointsofintrest(self):
        pass

    def sortbyfreq(self):
        pass