from jaratoolbox import celldatabase

subject = 'feat006'
experiments = []

# Experiment parameters: subject, date, brainArea, recordingTrack (penetrationLocationAndDye),
#    info (which contains [probeOrientation, soundSource, probeConfiguration]).
# Session parameters: sessionTime, behaviorFileSuffix, sessionType paradigmName.


exp0 = celldatabase.Experiment(subject, '2022-02-21', brainArea='AC_right', probe = 'NPv1-8131', recordingTrack='caudomedialDiI', info=['caudomedialDiI', 'soundLeft']) #reference = external
experiments.append(exp0)
# 11:15 in booth
# 11:30 couldn't penetrate brain. Retracted and tried cleaning craniotomy
# 11:45 tried lowering electrodes again. In brain
# 11:53 reached max depth
# 12:20 started recording
# 1:25 done

exp0.add_site(2934)
exp0.maxDepth = 2934
exp0.add_session('12-20-35','a','AM','am_tuning_curve') 
exp0.add_session('12-32-36','b','pureTones','am_tuning_curve')
exp0.add_session('12-49-24','a','FTVOTBorders','2afc_speech')

exp1 = celldatabase.Experiment(subject, '2022-02-22', brainArea='AC_right', probe = 'NPv1-8131', recordingTrack='middlemedialDiD', info=['middlemedialDiD', 'soundLeft']) #reference = external
experiments.append(exp1)
# 13:30 in booth
# 13:45 reached max depth
# 14:05 started recording
# 15:15 done

exp1.add_site(2963)
exp1.maxDepth = 2963
exp1.add_session('14-08-43','a','AM','am_tuning_curve') 
exp1.add_session('14-16-56','b','pureTones','am_tuning_curve')
exp1.add_session('14-34-15','a','FTVOTBorders','2afc_speech')


#exp2 = celldatabase.Experiment(subject, '2022-02-23', brainArea='AC_right', probe = 'NPv1-8131', recordingTrack='DiI', info=['DiI', 'soundLeft']) #reference = external
#experiments.append(exp2)
# 13:20 in booth
# 13:30 can't penetrate brain, trying cleaning craniotomy
# 14:40 still couldn't get in brain. cancelled recording

exp3 = celldatabase.Experiment(subject, '2022-02-24', brainArea='AC_left', probe = 'NPv1-8131', recordingTrack='caudomedialDiI', info=['caudomedialDiI', 'soundRight']) #reference = external
experiments.append(exp2)
# 11:35 in booth
# cleaned L craniotomy
# 12:25 in brain, reached max depth
# 12:41 started recording

exp3.add_site(2959)
exp3.maxDepth = 2959
exp3.add_session('12-40-52','a','AM','am_tuning_curve') 
exp3.add_session('12-49-15','b','pureTones','am_tuning_curve')
exp3.add_session('13-05-39','a','FTVOTBorders','2afc_speech')