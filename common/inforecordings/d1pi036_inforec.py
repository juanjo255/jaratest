from jaratoolbox import celldatabase
reload(celldatabase)

subject = 'd1pi036'
experiments=[]

exp0 = celldatabase.Experiment(subject, '2019-05-23', 'right_AudStr',
info=['PosteriorDiD', 'TT1left', 'soundLeft', 'A4x2-tet'])
experiments.append(exp0)

#50 noiseburst, 50 laser pulse, 40 laser train, 160 tuningTest, 1760 tc, 220 AM
#Used left speaker;laser (445 nm) set to 2.0 mW; Probe CEC2; Rig 2

"""
Laser Calibration
Power: Value on laser dial
0.5: 1.70
1.0: 2.60
1.5: 3.55
2.0: 4.20
2.5: 5.40
3.0: 7.60
3.5: 8.5
4.0: 10
"""

# Animal in rig at: 02:15
# Probe in at: 3:00

exp0.add_site(2900, tetrodes=[1,2,3,4,6])
exp0.add_session('15-16-41', None, 'noisebursts', 'am_tuning_curve')

exp0.add_site(3000, tetrodes=[1,2,3,4,6])
exp0.add_session('15-34-23', None, 'noisebursts', 'am_tuning_curve')

exp0.add_site(3100, tetrodes=[1,2,3,4,6])
exp0.add_session('16-02-51', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('16-07-29', None, 'laserpulse', 'am_tuning_curve')

exp0.add_site(3200, tetrodes=[1,2,3,4,6])
exp0.add_session('16-21-12', None, 'noisebursts', 'am_tuning_curve')
exp0.add_session('16-23-13', None, 'laserpulse', 'am_tuning_curve')

exp0.maxDepth = 3200


exp1 = celldatabase.Experiment(subject, '2019-05-29', 'left_AudStr',
info=['lateralDiD', 'TT1ant', 'soundRight', 'A4x2-tet'])
experiments.append(exp1)

#50 noiseburst, 50 laser pulse, 40 laser train, 240 tuningTest, 1760 tc, 220 AM
#Used right speaker;laser (445 nm) set to 2.5 mW; Probe CEC2; Rig 2

"""
Laser Calibration
Power: Value on laser dial
0.5: 1.50
1.0: 1.92
1.5: 2.45
2.0: 3.00
2.5: 3.62
3.0: 4.10
3.5: 4.95
4.0: 5.75
"""

# Animal in rig at: 11:51 AM
# Probe in at: 12:35 PM

exp1.add_site(2800, tetrodes=[2,3,4,5,6])
exp1.add_session('13-16-11', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('13-17-53', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('13-20-12', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('13-22-13', 'a', 'tuningTest', 'am_tuning_curve')
exp1.add_session('13-31-51', 'b', 'tuningCurve (tc)', 'am_tuning_curve')
exp1.add_session('14-09-39', 'c', 'am', 'am_tuning_curve')

exp1.add_site(2900, tetrodes=[1,3,4,5,6])
exp1.add_session('14-47-40', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('14-49-24', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('14-51-01', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('14-52-59', 'd', 'tuningTest', 'am_tuning_curve')
exp1.add_session('14-59-06', 'e', 'tuningCurve (tc)', 'am_tuning_curve')
exp1.add_session('15-30-32', 'f', 'am', 'am_tuning_curve')
exp1.add_session('15-37-54', None, 'laserpulse', 'am_tuning_curve')

exp1.add_site(3000, tetrodes=[1,3,4,5,6])
exp1.add_session('15-57-39', None, 'noisebursts', 'am_tuning_curve')
exp1.add_session('15-59-00', None, 'laserpulse', 'am_tuning_curve')
exp1.add_session('16-01-57', None, 'lasertrain', 'am_tuning_curve')
exp1.add_session('16-03-39', 'g', 'tuningTest', 'am_tuning_curve')
exp1.add_session('16-11-06', 'h', 'am', 'am_tuning_curve')

exp1.maxDepth = 3000
