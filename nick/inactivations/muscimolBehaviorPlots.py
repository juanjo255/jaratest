'''
For compiling the behavior data from muscimol and saline days
'''
import sys
from jaratest.nick import behavioranalysis_vnick as behavioranalysis
reload(behavioranalysis)
from matplotlib import pyplot as plt
# from jaratoolbox import behavioranalysis
reload(behavioranalysis)

# # subjects = ['amod001', 'amod002', 'amod003', 'amod004', 'amod005']

# if len(sys.argv)>1:
#     subject = sys.argv[1]
#     sessions = sys.argv[2:]
#     #sessions = input("Enter sessions (in a list of strings ['','']) to check behavior performance:")

# behavioranalysis.behavior_summary(subject,sessions,trialslim=[0,1000],outputDir='/home/nick/data/behavior_reports')


def muscimol_plot(animal,
                  muscimolSessions,
                  salineSessions,
                  mcolor='r',
                  scolor='k',
                  msty='-',
                  ssty='-'):
    muscimolData = behavioranalysis.load_many_sessions(animal, muscimolSessions)
    plineM, pcapsM, pbarsM, pdotsM = behavioranalysis.plot_frequency_psycurve(muscimolData)
    plt.setp(plineM, color=mcolor)
    plt.setp(pcapsM, color=mcolor)
    plt.setp(pbarsM, color=mcolor)
    plt.setp(pdotsM, markerfacecolor=mcolor)
    plt.setp(plineM, ls=msty)


    salineData = behavioranalysis.load_many_sessions(animal, salineSessions)
    plineS, pcapsS, pbarsS, pdotsS = behavioranalysis.plot_frequency_psycurve(salineData)
    plt.setp(plineS, color=scolor)
    plt.setp(pcapsS, color=scolor)
    plt.setp(pbarsS, color=scolor)
    plt.setp(pdotsS, markerfacecolor=scolor)
    plt.setp(plineS, ls=ssty)

    plt.title(animal)


if __name__=='__main__':
    plt.figure()
    animal = 'amod001'
    muscimolSessions = ['20160214a', '20160317a', '20160319a', '20160321a', '20160323a']
    salineSessions = ['20160315a', '20160318a', '20160320a', '20160322a']
    muscimol_plot(animal, muscimolSessions, salineSessions)

    plt.figure()
    animal = 'amod005'
    muscimolSessions = ['20160215a', '20160317a', '20160319a', '20160321a', '20160323a']
    salineSessions = ['20160316a', '20160318a', '20160320a', '20160322a']
    muscimol_plot(animal, muscimolSessions, salineSessions)

    plt.figure()
    animal = 'adap016'
    # muscimolSessions = ['20160317a', '20160319a', '20160321a']
    muscimolSessions = ['20160319a', '20160321a']
    salineSessions = ['20160316a', '20160318a', '20160320a', '20160322a']
    muscimol_plot(animal, muscimolSessions, salineSessions)

    plt.figure()
    animal = 'adap019'
    muscimolSessions = ['20160317a', '20160319a','20160323a']
    salineSessions = ['20160316a', '20160318a', '20160320a', '20160322a']
    muscimol_plot(animal, muscimolSessions, salineSessions)

    plt.figure()
    animal = 'adap019'
    # muscimolSessions = ['20160317a', '20160319a']
    muscimolSessions = ['20160322a']
    salineSessions = ['20160316a', '20160318a', '20160320a']
    muscimol_plot(animal, muscimolSessions, salineSessions)

    plt.figure()
