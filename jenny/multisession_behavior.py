import os
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from jaratoolbox import settings
from jaratoolbox import loadbehavior
from jaratoolbox import behavioranalysis

print('Enter which subjects you want to look at: 1 = VOT, 2 = FT, 3 = all, 4 = AM cohort, 5 = PM cohort or enter a specific animal name')
#print('Enter the subject name')
whichSubject = input()
if whichSubject == '1': #VOT cohort
    subject = ['bili034', 'bili035', 'bili036', 'bili037', 'bili038', 'bili039', 'bili040', 'bili041', 'bili042'] #VOT animals
elif whichSubject == '2': #FT cohort
    subject = ['bili043', 'bili044', 'bili045', 'bili046', 'bili047', 'bili048', 'bili049', 'bili050', 'bili051'] #FT animals
elif whichSubject == '3': #all
    subject = ['bili034', 'bili035', 'bili036', 'bili037', 'bili038', 'bili039', 'bili040', 'bili041', 'bili042', 'bili043', 'bili044', 'bili045', 'bili046', 'bili047', 'bili048', 'bili049', 'bili050', 'bili051']
elif whichSubject == '4': #AM cohort
    subject = ['bili034', 'bili035', 'bili036', 'bili037', 'bili038', 'bili048', 'bili049', 'bili050', 'bili051']
elif whichSubject == '5': #PM cohort
    subject = ['bili039', 'bili040', 'bili041', 'bili042', 'bili043', 'bili044', 'bili045', 'bili046', 'bili047']
else:
    subject = [whichSubject]

paradigm = '2afc_speech'

# Add the dates
sessions = []
#print('input the date of the first session you want to look at (e.g. 20220115):')
#firstSession = int(input())
firstSession = 20220115
print('input the last date of the sessions you want to look at (e.g. 20220121):')
lastSession = int(input())
dates = np.arange(firstSession,lastSession+1,1)
for nDates in range(len(dates)):
    sessions.append('{}a'.format(dates[nDates]))

#bdata = behavioranalysis.load_many_sessions(subject, sessions, paradigm)


for nSub in range(len(subject)): #np.unique(bdata['subjectID']):
    fig, ax = plt.subplots(figsize=(5,4),dpi=200)
    bdata = behavioranalysis.load_many_sessions(subject[nSub], sessions, paradigm)
    leftTrials = bdata['rewardSide'] == bdata.labels['rewardSide']['left']
    rightTrials = bdata['rewardSide'] == bdata.labels['rewardSide']['right']
    leftChoice = bdata['choice'] == bdata.labels['choice']['left']
    rightChoice = bdata['choice'] == bdata.labels['choice']['right']
    noChoice = bdata['choice'] == bdata.labels['choice']['none']

    sessionStart = 0
    subjPerformance = np.zeros((len(sessions),3))
    sessionLimits = np.zeros((len(sessions),2))
    for nSess in np.unique(bdata['sessionID']):
        #check if file exists, if it doesn't, set all performance = 0
        behavFile = loadbehavior.path_to_behavior_data(subject[nSub], paradigm, sessions[nSess])
        try:
            loadbehavior.BehaviorData(behavFile)
        except IOError:
            sessionLimits[nSess,:] = [0, 0]
            subjPerformance[nSess,:] = [0, 0, 0]
            endInd = int(sessionLimits[nSess,1])

        sessionEnd = sessionStart + sum(bdata['sessionID'] == nSess) - 1
        #if session is empty (zero trials) then set everything to 0
        if sessionEnd - sessionStart == 0:
            sessionLimits[nSess,:] = [sessionStart, sessionEnd]
            subjPerformance[nSess,:] = [0, 0, 0]
            plt.plot(sessions[nSess], subjPerformance[nSess,0],'ro', mfc ='r')
            plt.plot(sessions[nSess], subjPerformance[nSess,1], 'bo', mfc ='b')
            plt.plot(sessions[nSess], subjPerformance[nSess,2], 'ko', mfc ='k')
        #otherwise, calculate percent correct for Left, right and all trials
        else:
            leftCorrect = leftTrials[sessionStart:sessionEnd] & leftChoice[sessionStart:sessionEnd]
            leftError = leftTrials[sessionStart:sessionEnd] & rightChoice[sessionStart:sessionEnd]
            leftInvalid = leftTrials[sessionStart:sessionEnd] & noChoice[sessionStart:sessionEnd]
            rightCorrect = rightTrials[sessionStart:sessionEnd] & rightChoice[sessionStart:sessionEnd]
            rightError = rightTrials[sessionStart:sessionEnd] & leftChoice[sessionStart:sessionEnd]
            rightInvalid = rightTrials[sessionStart:sessionEnd] & noChoice[sessionStart:sessionEnd]
            rightPercentCorrect = round(sum(rightCorrect)/sum(rightTrials[sessionStart:sessionEnd])*100,2)
            leftPercentCorrect = round(sum(leftCorrect)/sum(leftTrials[sessionStart:sessionEnd])*100,2)
            totalPercentCorrect = round((sum(leftCorrect)+sum(rightCorrect))/(sum(leftTrials[sessionStart:sessionEnd]) + sum(rightTrials[sessionStart:sessionEnd]))*100,2)
            subjPerformance[nSess,:] = [rightPercentCorrect, leftPercentCorrect, totalPercentCorrect]
            sessionLimits[nSess,:] = [sessionStart, sessionEnd]
            sessionStart = sessionEnd + 1


    plt.title(subject[nSub])
    numDays = np.arange(0,nSess+1,1)
    line1, = ax.plot(numDays, subjPerformance[:,0],'r', label = "Right Trials")
    line2, = ax.plot(numDays, subjPerformance[:,1],'b', label = "Left Trials")
    line3, = ax.plot(numDays, subjPerformance[:,2],'k', label = "All Trials")
    ax.plot([50] * len(numDays), '0.5' ,linestyle = '--')


    for nSess in np.unique(bdata['sessionID']):
        endInd = int(sessionLimits[nSess,1])
        if bdata['outcomeMode'][endInd] == bdata.labels['outcomeMode']['only_if_correct']:
            if bdata['antibiasMode'][endInd] == bdata.labels['antibiasMode']['repeat_mistake']:
                ax.plot(numDays[nSess], subjPerformance[nSess,0],'ro', mfc = 'w' )
                ax.plot(numDays[nSess], subjPerformance[nSess,1], 'bo', mfc = 'w')
                dots1, = ax.plot(numDays[nSess], subjPerformance[nSess,2], 'ko', mfc ='w', label = "Antibiasmode ON")
            else:
                ax.plot(numDays[nSess], subjPerformance[nSess,0],'ro', mfc ='r')
                ax.plot(numDays[nSess], subjPerformance[nSess,1], 'bo', mfc ='b')
                dots2, = ax.plot(numDays[nSess], subjPerformance[nSess,2], 'ko', mfc ='k', label = "Antibiasmode OFF")

    plt.xlabel('Session Number')
    plt.ylabel('Percent Correct')
#    ax.legend([line1, line2])#,["rightTrials", "leftTrials"])
    labels = ['Right Trials', 'Left Trials', 'All Trials', 'Antibiasmode ON', 'Antibiasmode OFF']
    ax.legend([line1, line2, line3, dots1, dots2], labels, loc = 'upper left')
    plt.show()
#    input('press enter for next subject')
#    plt.close()
#plt.close()
