from jaratoolbox.test.nick.database import cellDB
reload(cellDB)
from jaratoolbox.test.lan.Ephys import sitefuncs_vlan as sitefuncs
reload(sitefuncs)

sessionTypes = {'nb':'noiseBurst',
                'lp':'laserPulse',
                'lt':'laserTrain',
                'tc':'tuningCurve',
                'bf':'bestFreq',
                '3p':'3mWpulse',
                '1p':'1mWpulse',
                '2afc':'2afc'}
'''
exp = cellDB.Experiment(animalName='test089', date ='2015-07-27', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-48-06', 'a', sessionTypes['tc'])
site1.add_session('16-03-24', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-07-28', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-39-35', 'a', sessionTypes['tc'])
site1.add_session('13-54-29', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-07-29', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('10-02-50', 'a', sessionTypes['tc'])
site1.add_session('10-26-08', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-07-30', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-14-33', 'a', sessionTypes['tc'])
site1.add_session('16-33-35', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-07-31', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-27-52', 'a', sessionTypes['tc'])
site1.add_session('14-40-40', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-01', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-24-02', 'a', sessionTypes['tc'])
site1.add_session('13-35-46', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-03', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-53-28', 'a', sessionTypes['tc'])
site1.add_session('16-12-32', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-04', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-10-06', 'a', sessionTypes['tc'])
site1.add_session('11-21-11', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-05', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-31-14', 'a', sessionTypes['tc'])
site1.add_session('16-44-02', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-06', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-04-36', 'a', sessionTypes['tc'])
site1.add_session('13-29-50', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-07', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-47-51', 'a', sessionTypes['tc'])
site1.add_session('16-05-00', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-10', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=1.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-06-35', 'a', sessionTypes['tc'])
site1.add_session('15-17-29', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-11', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.00, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-04-53', 'a', sessionTypes['tc'])
site1.add_session('11-14-14', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-12', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.00, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('23-11-37', 'a', sessionTypes['tc'])
site1.add_session('23-22-12', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-13', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.125, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-45-00', 'a', sessionTypes['tc'])
site1.add_session('16-59-59', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-14', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.125, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-03-20', 'b', sessionTypes['tc'])
site1.add_session('13-12-32', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-17', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.125, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-13-03', 'a', sessionTypes['tc'])
site1.add_session('15-22-05', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-18', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('17-20-28', 'a', sessionTypes['tc'])
site1.add_session('17-32-48', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-19', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-44-48', 'a', sessionTypes['tc'])
site1.add_session('12-53-30', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-20', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-39-56', 'a', sessionTypes['tc'])
site1.add_session('12-51-26', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
#################SAYS THERE IS SOME MISALIGNMENT IN THIS TRIAL (411 IS OUT OF BOUNDS FOR AXIS 1 WITH SIZE 411)
exp = cellDB.Experiment(animalName='test089', date ='2015-08-21', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-42-06', 'a', sessionTypes['tc'])
site1.add_session('16-54-19', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
exp = cellDB.Experiment(animalName='test089', date ='2015-08-27', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-47-43', 'a', sessionTypes['tc'])
site1.add_session('11-56-32', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-08-28', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-04-56', 'a', sessionTypes['tc'])
site1.add_session('11-14-17', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
##########THIS GOT A MEMORY ERROR WHILE CLUSTERING
exp = cellDB.Experiment(animalName='test089', date ='2015-08-31', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-59-13', 'a', sessionTypes['tc'])
site1.add_session('16-14-28', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
exp = cellDB.Experiment(animalName='test089', date ='2015-09-01', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-56-47', 'a', sessionTypes['tc'])
site1.add_session('14-06-28', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-02', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.500, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-25-18', 'a', sessionTypes['tc'])
site1.add_session('14-34-43', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-09', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.500, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-19-59', 'a', sessionTypes['tc'])
site1.add_session('13-29-23', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-10', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-24-35', 'a', sessionTypes['tc'])
site1.add_session('12-37-41', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-11', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-19-19', 'a', sessionTypes['tc'])
site1.add_session('12-33-17', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-13', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-49-37', 'a', sessionTypes['tc'])
site1.add_session('16-00-43', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-14', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('17-50-55', 'a', sessionTypes['tc'])
site1.add_session('18-02-42', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-15', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-23-20', 'a', sessionTypes['tc'])
site1.add_session('12-41-17', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-17', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-06-01', 'c', sessionTypes['tc'])
site1.add_session('14-19-06', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-18', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-50-42', 'a', sessionTypes['tc'])
site1.add_session('13-00-00', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-21', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-08-09', 'a', sessionTypes['tc'])
site1.add_session('12-23-48', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-23', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=2.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-32-17', 'a', sessionTypes['tc'])
site1.add_session('12-45-45', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-24', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-23-14', 'a', sessionTypes['tc'])
site1.add_session('13-32-28', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-09-25', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-30-40', 'a', sessionTypes['tc'])
site1.add_session('12-41-02', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

#######THIS SESSION HAS NO TUNING CURVE AND GND WIRE CAME LOOSE SO HAS SPEAKER NOISE
exp = cellDB.Experiment(animalName='test089', date ='2015-09-26', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-03-31', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-10-08', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-37-12', 'a', sessionTypes['tc'])
site1.add_session('13-51-27', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-10-09', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-25-21', 'a', sessionTypes['tc'])
site1.add_session('11-41-20', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-10-14', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-00-10', 'a', sessionTypes['tc'])
site1.add_session('11-09-05', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-02', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-05-35', 'a', sessionTypes['tc'])
site1.add_session('11-20-25', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-04', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('20-07-25', 'a', sessionTypes['tc'])
site1.add_session('20-16-21', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-07', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-36-26', 'a', sessionTypes['tc'])
site1.add_session('11-45-08', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-08', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.125, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-29-01', 'a', sessionTypes['tc'])
site1.add_session('11-37-49', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-09', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-13-35', 'a', sessionTypes['tc'])
site1.add_session('11-22-28', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-10', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-34-02', 'a', sessionTypes['tc'])
site1.add_session('11-43-39', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-11', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.50, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-22-03', 'a', sessionTypes['tc'])
site1.add_session('11-31-06', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-13', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('18-44-45', 'a', sessionTypes['tc'])
site1.add_session('18-54-08', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-14', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-11-22', 'a', sessionTypes['tc'])
site1.add_session('14-22-50', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-15', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-20-59', 'a', sessionTypes['tc'])
site1.add_session('16-29-48', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-16', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-47-56', 'a', sessionTypes['tc'])
site1.add_session('15-56-35', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-17', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-08-07', 'a', sessionTypes['tc'])
site1.add_session('14-16-40', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-18', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-33-26', 'a', sessionTypes['tc'])
site1.add_session('13-41-51', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-21', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('12-36-50', 'a', sessionTypes['tc'])
site1.add_session('12-45-50', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-22', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-57-24', 'a', sessionTypes['tc'])
site1.add_session('15-06-18', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2015-12-23', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-14-01', 'a', sessionTypes['tc'])
site1.add_session('14-22-34', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-11', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-44-37', 'a', sessionTypes['tc'])
site1.add_session('16-55-08', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-12', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-44-21', 'a', sessionTypes['tc'])
site1.add_session('13-52-50', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-13', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=3.875, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-33-11', 'a', sessionTypes['tc'])
site1.add_session('15-41-48', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-14', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.000, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('10-35-18', 'a', sessionTypes['tc'])
site1.add_session('10-45-25', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-15', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.125, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('10-52-21', 'a', sessionTypes['tc'])
site1.add_session('11-03-35', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-16', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-03-42', 'a', sessionTypes['tc'])
site1.add_session('15-12-13', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-18', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-55-09', 'a', sessionTypes['tc'])
site1.add_session('16-03-39', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
####CRASHED IN CLUSTERING. TIMES OF EVENTS ARE NOT ORDERED
exp = cellDB.Experiment(animalName='test089', date ='2016-01-19', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('17-18-18', 'a', sessionTypes['tc'])
site1.add_session('17-27-25', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
exp = cellDB.Experiment(animalName='test089', date ='2016-01-20', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-35-55', 'a', sessionTypes['tc'])
site1.add_session('16-44-25', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-21', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-54-52', 'a', sessionTypes['tc'])
site1.add_session('14-03-15', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-22', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.25, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-46-21', 'a', sessionTypes['tc'])
site1.add_session('14-54-43', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-23', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.375, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-09-57', 'a', sessionTypes['tc'])
site1.add_session('16-18-45', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-24', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.50, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('16-37-23', 'a', sessionTypes['tc'])
site1.add_session('16-46-10', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-25', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.50, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-55-26', 'a', sessionTypes['tc'])
site1.add_session('15-03-55', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-26', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-20-06', 'a', sessionTypes['tc'])
site1.add_session('14-28-41', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-27', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('15-33-25', 'a', sessionTypes['tc'])
site1.add_session('15-41-59', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-28', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.625, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('14-11-05', 'a', sessionTypes['tc'])
site1.add_session('14-23-09', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-29', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-57-12', 'a', sessionTypes['tc'])
site1.add_session('12-07-45', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-01-30', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-01-55', 'a', sessionTypes['tc'])
site1.add_session('13-10-40', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-02-01', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-44-37', 'a', sessionTypes['tc'])
site1.add_session('13-53-07', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-02-02', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('10-45-36', 'a', sessionTypes['tc'])
site1.add_session('10-53-55', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-02-03', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('11-29-15', 'a', sessionTypes['tc'])
site1.add_session('11-39-32', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-02-08', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('10-38-26', 'a', sessionTypes['tc'])
site1.add_session('10-49-39', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)

exp = cellDB.Experiment(animalName='test089', date ='2016-02-09', experimenter='', defaultParadigm='tuning_curve')
site1 = exp.add_site(depth=4.75, tetrodes=[1,2,3,4,5,6,7,8])
site1.add_session('13-59-14', 'a', sessionTypes['tc'])
site1.add_session('14-08-15', 'a', sessionTypes['2afc'], paradigm='2afc')
sitefuncs.nick_lan_daily_report_v2(site1, 'site1', mainRasterInds=None, mainTCind=0)
'''
