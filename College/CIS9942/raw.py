#!/usr/bin/env python3

import logging
log = logging.getLogger(__name__)
log.info('Instance of ' + __name__)

raw = """[LongName]
1-6G 18V Horiz Site H 16point
[Configuration]
{SignalSource}
Signal.Source=IEEE
Signal.IEEEPort=19
Signal.DriverFile=esg3000g.sig
Signal.Serial=
{Switch}
Switch.Source=
Switch.DriverFile=
Switch.Serial=
{Switch2}
Switch2.Source=
Switch2.DriverFile=
Switch2.Serial=
{Amplifier2}
Amp2.Source=
Amp2.DriverFile=
Amp2.Serial=
{Amplifier3}
Amp3.Source=
Amp3.DriverFile=
Amp3.Serial=
{PowerMonitor}
PowerMon.Source=IEEE
PowerMon.IEEEPort=17
PowerMon.Units=
PowerMon.DriverFile=hp436b.pow
PowerMon.Serial=
PowerMon.Factors=
PowerMon.FactorsSerial=
PowerMon.Factors2=
PowerMon.FactorsSerial2=
PowerMon.Formula=x+(-0.0000000024*(f))+40.4
PowerMon.Limit=
PowerMon.FieldInc=0.0
PowerMon.FieldDrop=0.0
{StressMeasure}
Stress.Source=RS232
Stress.ComPort= 2
Stress.Units=V/m
Stress.DriverFile=emr-20.sen
Stress.Serial=
Stress.Factors=
Stress.FactorsSerial=
Stress.Formula=
{Amplifier}
Amp.Source=
Amp.DriverFile=1-6.amp
Amp.Serial=
{TransAntenna}
Trans.DriverFile=
Trans.Serial=
{Limiter}
Limiter.Source=
Limiter.Units=
Limiter.DriverFile=
Limiter.Serial=
Limiter.Factors=
Limiter.FactorsSerial=
Limiter.Formula=
Limiter.Limit=
Limiter.FieldInc=0.0
Limiter.FieldDrop=0.0
{PowerMonitor2}
PowerMon2.Source=
PowerMon2.Units=
PowerMon2.DriverFile=
PowerMon2.Serial=
PowerMon2.Factors=
PowerMon2.FactorsSerial=
PowerMon2.Factors2=
PowerMon2.FactorsSerial2=
PowerMon2.Formula=
PowerMon2.Limit=
PowerMon2.FieldInc=0.0
PowerMon2.FieldDrop=0.0
{Positioner}
Pos.Source=
Pos.DriverFile=
[Setup]
ConfigFile=
CalFile=
SweepType=Incremental
ManualControl= 0
LevellingMethod=Power
FreqFontName=Arial
FreqFontSize= 10
FreqFontBold= 0
FreqFontItalic= 0
FreqFontUnderline= 0
FreqFontStrikethru= 0
FreqFontColour= 255
FreqScale= 1
{Segment}
Seg0.StartFreq=1000000000.000
Seg0.StopFreq=6000000000.000
Seg0.SweepScale=Log
Seg0.FreqInc=1.000
Seg0.SigLevInc=6.0
Seg0.SensorLevel=18.000
Seg0.LevellingWindow=5
Seg0.DwellTime=0.300
Seg0.AmpMod=0
Seg0.GenMin=-60.0
Seg0.GenMax=10.0
Seg0.FieldDrop=0.0
Seg0.DropDec=0.0
Seg0.DropTime=0.000
Seg0.FieldMove=0.0
{SpotFreq}
926445000.000
{TableHeader}
Col0.Title=Frequency
Col0.Type=Frequency
Col0.Width=-1
Col1.Title=Target Stress
Col1.Type=Target
Col1.Width=-1
Col2.Title=Actual Stress
Col2.Type=Level
Col2.Width=-1
Col2.Plot=-1
Col2.PlotColour= 0
Col2.PlotTitle=RF Stress %
Col2.PlotStyle= 0
Col2.PlotMin= 0
Col2.PlotMax= 100
Col2.PlotInPercent=-1
Col2.PlotFontName=Arial
Col2.PlotFontSize= 10
Col2.PlotFontBold= 0
Col2.PlotFontItalic= 0
Col2.PlotFontUnderline= 0
Col2.PlotFontStrikethru= 0
Col3.Title=Generator Level
Col3.Type=DriveLevel
Col3.Width=-1
Col3.Plot= 0
Col4.Title=Forward Power
Col4.Type=ForwardPower
Col4.Width=-1
Col4.Plot=-1
Col4.PlotColour= 32768
Col4.PlotTitle=Fwd
Col4.PlotStyle= 0
Col4.PlotMin=-50
Col4.PlotMax= 50
Col4.PlotFontName=Arial
Col4.PlotFontSize= 10
Col4.PlotFontBold= 0
Col4.PlotFontItalic= 0
Col4.PlotFontUnderline= 0
Col4.PlotFontStrikethru= 0
Col5.Title=Reverse Power
Col5.Type=ReversePower
Col5.Width=-1
Col5.Plot= 0
Col6.Title=Net Power
Col6.Type=NetPower
Col6.Width=-1
Col6.Plot= 0
[Calibration]
Date=07/08/2016
Time=14:40
Operator=
SetupFileName=C:\CIS9942\SETUPS\00-4-3.SET
SetupLongName=1000-4-3 10V
{Data}
 1.000 GHz 	 18.450 	 18.450 	 -7.3 	 43.26
 1.010 GHz 	 18.450 	 18.450 	 -6.3 	 43.77
 1.020 GHz 	 18.450 	 18.450 	 -5.7 	 43.63
 1.030 GHz 	 18.450 	 18.450 	 -6.0 	 44.10
 1.041 GHz 	 18.450 	 18.450 	 -6.6 	 43.19
 1.051 GHz 	 18.450 	 18.450 	 -7.5 	 42.76
 1.062 GHz 	 18.450 	 18.450 	 -6.8 	 43.08
 1.072 GHz 	 18.450 	 18.450 	 -5.0 	 44.05
 1.083 GHz 	 18.450 	 18.450 	 -3.9 	 45.51
 1.094 GHz 	 18.450 	 18.450 	 -3.8 	 44.81
 1.105 GHz 	 18.450 	 18.450 	 -4.5 	 44.56
 1.116 GHz 	 18.450 	 18.450 	 -3.9 	 45.44
 1.127 GHz 	 18.450 	 18.450 	 -4.2 	 44.96
 1.138 GHz 	 18.450 	 18.450 	 -5.0 	 43.98
 1.149 GHz 	 18.450 	 18.450 	 -5.3 	 44.22
 1.161 GHz 	 18.450 	 18.450 	 -4.3 	 44.45
 1.173 GHz 	 18.450 	 18.450 	 -3.3 	 45.98
 1.184 GHz 	 18.450 	 18.450 	 -2.3 	 46.22
 1.196 GHz 	 18.450 	 18.450 	 -2.4 	 46.56
 1.208 GHz 	 18.450 	 18.450 	 -2.1 	 46.34
 1.220 GHz 	 18.450 	 18.450 	 -0.5 	 46.62
 1.232 GHz 	 18.450 	 18.450 	 -0.6 	 46.61
 1.245 GHz 	 18.450 	 18.450 	 -1.0 	 46.87
 1.257 GHz 	 18.450 	 18.450 	 1.3 	 48.20
 1.270 GHz 	 18.450 	 18.450 	 0.4 	 47.30
 1.282 GHz 	 18.450 	 18.450 	 0.4 	 48.09
 1.295 GHz 	 18.450 	 18.450 	 -0.4 	 47.49
 1.308 GHz 	 18.450 	 18.450 	 -1.6 	 47.36
 1.321 GHz 	 18.450 	 18.450 	 -2.2 	 46.94
 1.335 GHz 	 18.450 	 18.450 	 -2.8 	 46.86
 1.348 GHz 	 18.450 	 18.450 	 -2.2 	 47.30
 1.361 GHz 	 18.450 	 18.450 	 -4.4 	 45.60
 1.375 GHz 	 18.450 	 18.450 	 -3.5 	 46.13
 1.389 GHz 	 18.450 	 18.450 	 -5.6 	 44.45
 1.403 GHz 	 18.450 	 18.450 	 -4.7 	 45.11
 1.417 GHz 	 18.450 	 18.450 	 -4.3 	 45.53
 1.431 GHz 	 18.450 	 18.450 	 -5.0 	 44.96
 1.445 GHz 	 18.450 	 18.450 	 -4.2 	 45.58
 1.460 GHz 	 18.450 	 18.450 	 -3.7 	 45.51
 1.474 GHz 	 18.450 	 18.450 	 -4.2 	 45.31
 1.489 GHz 	 18.450 	 18.450 	 -3.7 	 45.06
 1.504 GHz 	 18.450 	 18.450 	 -2.3 	 45.28
 1.519 GHz 	 18.450 	 18.450 	 -1.6 	 46.07
 1.534 GHz 	 18.450 	 18.450 	 -1.3 	 46.45
 1.549 GHz 	 18.450 	 18.450 	 -0.1 	 46.92
 1.565 GHz 	 18.450 	 18.450 	 0.1 	 47.47
 1.580 GHz 	 18.450 	 18.450 	 3.2 	 48.13
 1.596 GHz 	 18.450 	 18.450 	 1.8 	 48.68
 1.612 GHz 	 18.450 	 18.450 	 2.1 	 47.44
 1.628 GHz 	 18.450 	 18.450 	 1.5 	 46.70
 1.645 GHz 	 18.450 	 18.450 	 -0.4 	 46.64
 1.661 GHz 	 18.450 	 18.450 	 0.4 	 46.30
 1.678 GHz 	 18.450 	 18.450 	 -1.0 	 45.59
 1.694 GHz 	 18.450 	 18.450 	 -1.2 	 45.36
 1.711 GHz 	 18.450 	 18.450 	 2.2 	 46.22
 1.729 GHz 	 18.450 	 18.450 	 -1.3 	 45.65
 1.746 GHz 	 18.450 	 18.450 	 0.4 	 44.86
 1.763 GHz 	 18.450 	 18.450 	 -0.3 	 44.88
 1.781 GHz 	 18.450 	 18.450 	 -0.9 	 44.42
 1.799 GHz 	 18.450 	 18.450 	 0.1 	 44.40
 1.817 GHz 	 18.450 	 18.450 	 -0.3 	 43.29
 1.835 GHz 	 18.450 	 18.450 	 -0.1 	 43.50
 1.853 GHz 	 18.450 	 18.450 	 1.2 	 43.76
 1.872 GHz 	 18.450 	 18.450 	 5.3 	 45.20
 1.890 GHz 	 18.450 	 18.450 	 5.7 	 47.15
 1.909 GHz 	 18.450 	 18.450 	 2.4 	 47.38
 1.928 GHz 	 18.450 	 18.450 	 2.6 	 45.84
 1.948 GHz 	 18.450 	 18.450 	 2.8 	 46.58
 1.967 GHz 	 18.450 	 18.450 	 0.9 	 45.29
 1.987 GHz 	 18.450 	 18.450 	 -0.6 	 45.52
 2.007 GHz 	 18.450 	 18.450 	 1.8 	 46.33
 2.027 GHz 	 18.450 	 18.450 	 3.8 	 45.90
 2.047 GHz 	 18.450 	 18.450 	 0.5 	 45.26
 2.068 GHz 	 18.450 	 18.450 	 0.9 	 46.01
 2.088 GHz 	 18.450 	 18.450 	 3.3 	 45.69
 2.109 GHz 	 18.450 	 18.450 	 5.5 	 45.89
 2.130 GHz 	 18.450 	 18.450 	 6.1 	 46.56
 2.152 GHz 	 18.450 	 18.450 	 2.4 	 46.42
 2.173 GHz 	 18.450 	 18.450 	 3.0 	 45.61
 2.195 GHz 	 18.450 	 18.450 	 4.6 	 47.26
 2.217 GHz 	 18.450 	 18.450 	 9.9 	 48.07
 2.239 GHz 	 18.450 	 18.450 	 8.0 	 47.93
 2.261 GHz 	 18.450 	 18.450 	 7.2 	 49.21
 2.284 GHz 	 18.450 	 18.450 	 6.0 	 48.25
 2.307 GHz 	 18.450 	 18.450 	 5.4 	 47.92
 2.330 GHz 	 18.450 	 18.450 	 5.2 	 48.74
 2.353 GHz 	 18.450 	 18.450 	 5.6 	 48.49
 2.377 GHz 	 18.450 	 18.450 	 6.9 	 48.02
 2.400 GHz 	 18.450 	 18.450 	 6.6 	 47.44
 2.424 GHz 	 18.450 	 18.450 	 6.2 	 46.83
 2.449 GHz 	 18.450 	 18.450 	 7.2 	 46.69
 2.473 GHz 	 18.450 	 18.450 	 6.9 	 46.72
 2.498 GHz 	 18.450 	 18.450 	 5.6 	 46.80
 2.523 GHz 	 18.450 	 18.450 	 6.1 	 46.79
 2.548 GHz 	 18.450 	 18.450 	 7.1 	 48.00
 2.574 GHz 	 18.450 	 18.450 	 6.2 	 47.24
 2.599 GHz 	 18.450 	 18.450 	 6.3 	 46.65
 2.625 GHz 	 18.450 	 18.450 	 5.7 	 46.74
 2.652 GHz 	 18.450 	 18.450 	 5.9 	 47.11
 2.678 GHz 	 18.450 	 18.450 	 5.1 	 46.51
 2.705 GHz 	 18.450 	 18.450 	 4.4 	 45.74
 2.732 GHz 	 18.450 	 18.450 	 4.9 	 46.48
 2.759 GHz 	 18.450 	 18.450 	 3.9 	 46.31
 2.787 GHz 	 18.450 	 18.450 	 4.2 	 46.48
 2.815 GHz 	 18.450 	 18.450 	 4.3 	 46.42
 2.843 GHz 	 18.450 	 18.450 	 6.4 	 47.27
 2.871 GHz 	 18.450 	 18.450 	 5.4 	 46.87
 2.900 GHz 	 18.450 	 18.450 	 9.6 	 47.04
 2.929 GHz 	 18.450 	 18.450 	 8.1 	 47.14
 2.958 GHz 	 18.450 	 18.450 	 7.4 	 47.52
 2.988 GHz 	 18.450 	 18.450 	 7.5 	 47.41
 3.018 GHz 	 18.450 	 18.450 	 4.9 	 47.21
 3.048 GHz 	 18.450 	 18.450 	 3.8 	 45.91
 3.078 GHz 	 18.450 	 18.450 	 4.1 	 46.34
 3.109 GHz 	 18.450 	 18.450 	 4.2 	 46.15
 3.140 GHz 	 18.450 	 18.450 	 7.3 	 45.30
 3.172 GHz 	 18.450 	 18.450 	 7.7 	 45.69
 3.203 GHz 	 18.450 	 18.450 	 4.0 	 45.50
 3.235 GHz 	 18.450 	 18.450 	 4.7 	 45.90
 3.268 GHz 	 18.450 	 18.450 	 5.3 	 46.44
 3.300 GHz 	 18.450 	 18.450 	 4.0 	 46.22
 3.333 GHz 	 18.450 	 18.450 	 3.1 	 45.67
 3.367 GHz 	 18.450 	 18.450 	 5.3 	 46.00
 3.400 GHz 	 18.450 	 18.450 	 4.8 	 45.61
 3.434 GHz 	 18.450 	 18.450 	 7.7 	 45.51
 3.469 GHz 	 18.450 	 18.450 	 7.2 	 45.13
 3.503 GHz 	 18.450 	 18.450 	 9.6 	 45.09
 3.538 GHz 	 18.450 	 18.450 	 8.2 	 44.86
 3.574 GHz 	 18.450 	 18.450 	 6.1 	 44.44
 3.610 GHz 	 18.450 	 18.450 	 4.7 	 43.92
 3.646 GHz 	 18.450 	 18.450 	 5.0 	 44.12
 3.682 GHz 	 18.450 	 18.450 	 4.7 	 44.05
 3.719 GHz 	 18.450 	 18.450 	 5.0 	 44.37
 3.756 GHz 	 18.450 	 18.450 	 4.9 	 44.57
 3.794 GHz 	 18.450 	 18.450 	 4.2 	 43.59
 3.832 GHz 	 18.450 	 18.450 	 4.6 	 43.50
 3.870 GHz 	 18.450 	 18.450 	 3.3 	 42.40
 3.909 GHz 	 18.450 	 18.450 	 4.0 	 43.37
 3.948 GHz 	 18.450 	 18.450 	 4.0 	 42.90
 3.987 GHz 	 18.450 	 18.450 	 5.7 	 43.05
 4.027 GHz 	 18.450 	 18.450 	 3.8 	 43.51
 4.067 GHz 	 18.450 	 18.450 	 5.7 	 43.85
 4.108 GHz 	 18.450 	 18.450 	 4.8 	 43.92
 4.149 GHz 	 18.450 	 18.450 	 4.0 	 42.67
 4.191 GHz 	 18.450 	 18.450 	 4.5 	 42.19
 4.233 GHz 	 18.450 	 18.450 	 2.9 	 41.99
 4.275 GHz 	 18.450 	 18.450 	 3.7 	 41.84
 4.318 GHz 	 18.450 	 18.450 	 3.0 	 40.59
 4.361 GHz 	 18.450 	 18.450 	 3.3 	 40.73
 4.404 GHz 	 18.450 	 18.450 	 2.7 	 39.67
 4.448 GHz 	 18.450 	 18.450 	 4.0 	 40.35
 4.493 GHz 	 18.450 	 18.450 	 4.2 	 39.78
 4.538 GHz 	 18.450 	 18.450 	 5.6 	 41.16
 4.583 GHz 	 18.450 	 18.450 	 3.0 	 39.97
 4.629 GHz 	 18.450 	 18.450 	 5.0 	 40.93
 4.675 GHz 	 18.450 	 18.450 	 2.2 	 39.04
 4.722 GHz 	 18.450 	 18.450 	 3.1 	 40.19
 4.769 GHz 	 18.450 	 18.450 	 0.6 	 37.91
 4.817 GHz 	 18.450 	 18.450 	 2.7 	 39.06
 4.865 GHz 	 18.450 	 18.450 	 0.4 	 36.18
 4.914 GHz 	 18.450 	 18.450 	 1.9 	 36.67
 4.963 GHz 	 18.450 	 18.450 	 2.0 	 35.46
 5.013 GHz 	 18.450 	 18.450 	 2.1 	 36.30
 5.063 GHz 	 18.450 	 18.450 	 2.5 	 36.30
 5.113 GHz 	 18.450 	 18.450 	 3.0 	 37.66
 5.164 GHz 	 18.450 	 18.450 	 2.2 	 37.21
 5.216 GHz 	 18.450 	 18.450 	 1.1 	 37.53
 5.268 GHz 	 18.450 	 18.450 	 -0.3 	 36.74
 5.321 GHz 	 18.450 	 18.450 	 0.4 	 37.17
 5.374 GHz 	 18.450 	 18.450 	 -0.9 	 35.19
 5.428 GHz 	 18.450 	 18.450 	 -1.0 	 33.53
 5.482 GHz 	 18.450 	 18.450 	 2.0 	 35.00
 5.537 GHz 	 18.450 	 18.450 	 4.0 	 35.39
 5.592 GHz 	 18.450 	 18.450 	 4.0 	 34.63
 5.648 GHz 	 18.450 	 18.450 	 6.9 	 36.27
 5.705 GHz 	 18.450 	 18.450 	 8.6 	 36.84
 5.762 GHz 	 18.450 	 18.450 	 9.7 	 38.00
 5.819 GHz 	 18.450 	 18.450 	 8.8 	 37.10
 5.878 GHz 	 18.450 	 18.450 	 9.4 	 35.57
 5.936 GHz 	 18.450 	 18.450 	 7.7 	 33.89
 5.996 GHz 	 18.450 	 18.450 	 8.7 	 34.15
 6.000 GHz 	 18.450 	 18.450 	 7.6 	 34.06 """
