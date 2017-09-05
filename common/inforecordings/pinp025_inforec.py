from jaratoolbox import celldatabase

subject = 'pinp025'
experiments = []

exp0 = celldatabase.Experiment(subject,
                               '2017-09-01',
                               brainarea='rightAstr',
                               info=['anteriorDiI', 'facingPosterior'])
experiments.append(exp0)

# Probe at 1583, waiting 10 mins

exp0.add_site(2012, tetrodes=range(1, 9)).remove_tetrodes([1])
# exp0.add_session('16-42-05', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('16-45-07', 'a', 'tc', 'am_tuning_curve')
exp0.add_session('17-18-45', 'b', 'am', 'am_tuning_curve')
exp0.add_session('17-34-28', None, 'noiseburst', 'am_tuning_curve')

exp0.add_site(2111, tetrodes=range(1, 9)).remove_tetrodes([1])
exp0.add_session('17-41-12', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('17-43-34', 'c', 'tc', 'am_tuning_curve')
exp0.add_session('18-17-49', 'd', 'am', 'am_tuning_curve')

exp0.add_site(2229, tetrodes=range(1, 9)).remove_tetrodes([1])
exp0.add_session('18-51-47', None, 'noiseburst', 'am_tuning_curve')
exp0.add_session('18-54-55','e', 'tc', 'am_tuning_curve')
exp0.add_session('19-30-23', 'f', 'am', 'am_tuning_curve')
# Done for the day



exp1 = celldatabase.Experiment(subject,
                               '2017-09-04',
                               brainarea='rightAstr',
                               info=['anteriorDiD', 'facingPosterior'])
experiments.append(exp1)

#Probe in at 10:36am
#Probe at 1909, waiting 10 mins

exp1.add_site(1990, tetrodes=range(1, 9)).remove_tetrodes([1])
exp1.add_session('11-07-18', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('11-11-46', 'a', 'tc', 'am_tuning_curve')
exp1.add_session('11-45-00', 'b', 'am', 'am_tuning_curve')

exp1.add_site(2051, tetrodes=range(1, 9)).remove_tetrodes([1])
exp1.add_session('12-09-49', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('12-12-35', 'c', 'tc', 'am_tuning_curve')
exp1.add_session('12-58-30', 'd', 'am', 'am_tuning_curve')

exp1.add_site(2163, tetrodes=range(1, 9)).remove_tetrodes([1])
exp1.add_session('13-24-25', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('13-29-30', 'e', 'tc', 'am_tuning_curve')
exp1.add_session('14-01-52', 'f', 'am', 'am_tuning_curve')

exp1.add_site(2271, tetrodes=range(1, 9)).remove_tetrodes([1])
exp1.add_session('14-22-48', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('14-25-44', 'g', 'tc', 'am_tuning_curve')
exp1.add_session('14-58-44', 'h', 'am', 'am_tuning_curve')

exp1.add_site(2406, tetrodes=range(1, 9)).remove_tetrodes([1, 2])
exp1.add_session('15-25-59', None, 'noiseburst', 'am_tuning_curve')
exp1.add_session('15-29-10', 'i', 'tc', 'am_tuning_curve')
exp1.add_session('16-02-16', 'j', 'am', 'am_tuning_curve')

exp1.add_site(2598, tetrodes=range(1, 9)).remove_tetrodes([1, 2])
exp1.add_session('16-31-14', None, 'noiseburst', 'am_tuning_curve')
# exp1.add_session('15-29-10', 'i', 'tc', 'am_tuning_curve')
# exp1.add_session('16-02-16', 'j', 'am', 'am_tuning_curve')
