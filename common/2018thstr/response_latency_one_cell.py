import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from jaratoolbox import celldatabase
from jaratoolbox import ephyscore
from jaratoolbox import spikesanalysis
reload(spikesanalysis)
from jaratoolbox import behavioranalysis
from jaratoolbox import settings
import figparams

threshold = 0.2

dbPath = os.path.join(settings.FIGURES_DATA_PATH, figparams.STUDY_NAME, 'celldatabase.h5')
dbase = pd.read_hdf(dbPath, key='dataframe')

cellDict = {'subject' : 'pinp017',
            'date' : '2017-03-22',
            'depth' : 1143,
            'tetrode' : 2,
            'cluster' : 4}

cellInd, dbRow = celldatabase.find_cell(dbase, **cellDict)
cell = ephyscore.Cell(dbRow)

try:
    ephysData, bdata = cell.load('tc')
except (IndexError, ValueError): #The cell does not have a tc or the tc session has no spikes
    print "No tc for cell {}".format(indRow)
    sys.exit()

eventOnsetTimes = ephysData['events']['soundDetectorOn']

eventOnsetTimes = spikesanalysis.minimum_event_onset_diff(eventOnsetTimes, minEventOnsetDiff=0.2)
spikeTimes = ephysData['spikeTimes']
freqEachTrial = bdata['currentFreq']
possibleFreq = np.unique(freqEachTrial)
intensityEachTrial = bdata['currentIntensity']
possibleIntensity = np.unique(intensityEachTrial)

#FIXME: I need to remove the last event here if there is an extra one
if len(eventOnsetTimes) == len(freqEachTrial)+1:
    eventOnsetTimes = eventOnsetTimes[:-1]

trialsEachCondition = behavioranalysis.find_trials_each_combination(intensityEachTrial, possibleIntensity,
                                                                    freqEachTrial, possibleFreq)

baseRange = [-0.1, 0]
responseRange = [0, 0.1]
alignmentRange = [-0.2, 0.2]

#Align all spikes to events
(spikeTimesFromEventOnset,
trialIndexForEachSpike,
indexLimitsEachTrial) = spikesanalysis.eventlocked_spiketimes(spikeTimes,
                                                            eventOnsetTimes,
                                                            alignmentRange)

#Count spikes in baseline and response ranges
nspkBase = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnset,
                                                    indexLimitsEachTrial,
                                                    baseRange)
nspkResp = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnset,
                                                    indexLimitsEachTrial,
                                                    responseRange)

#Filter and average the response spikes by the condition matrix
conditionMatShape = np.shape(trialsEachCondition)
numRepeats = np.product(conditionMatShape[1:])
nSpikesMat = np.reshape(nspkResp.squeeze().repeat(numRepeats), conditionMatShape)
spikesFilteredByTrialType = nSpikesMat * trialsEachCondition
avgRespArray = np.sum(spikesFilteredByTrialType, 0) / np.sum(
    trialsEachCondition, 0).astype('float')

thresholdResponse = nspkBase.mean() + threshold*(avgRespArray.max()-nspkBase.mean())

if not np.any(avgRespArray > thresholdResponse):
    print "Nothing above the threshold"
    sys.exit()

#Determine trials that come from a I/F pair with a response above the threshold
fra = avgRespArray > thresholdResponse
selectedTrials = np.any(trialsEachCondition[:,fra], axis=1)

# -- Calculate response latency --
indexLimitsSelectedTrials = indexLimitsEachTrial[:,selectedTrials]
timeRangeForLatency = [-0.1,0.1]
(respLatency,interim) = spikesanalysis.response_latency(spikeTimesFromEventOnset,
                                                        indexLimitsSelectedTrials,
                                                        timeRangeForLatency, threshold=0.5)


print 'Response latency: {:0.1f} ms'.format(1e3*respLatency)

# ------------ From here down is for plotting -------------
selectedTrialsInds = np.flatnonzero(selectedTrials)
selectedSpikesInds = np.isin(trialIndexForEachSpike,selectedTrialsInds)
tempTIFES = trialIndexForEachSpike[selectedSpikesInds]
newSpikeTimes = spikeTimesFromEventOnset[selectedSpikesInds]

# The next thing is slow, but I don't have time to optimize
newTrialInds = np.empty(tempTIFES.shape, dtype=int)
for ind,trialInd in enumerate(np.unique(tempTIFES)):
    newTrialInds[tempTIFES==trialInd] = ind

plt.clf()
plt.title(cellInd)
plt.subplot(2,1,1)
plt.plot(newSpikeTimes, newTrialInds, '.k')
#plt.plot(spikeTimesFromEventOnset, trialIndexForEachSpike, '.k') # Plot all trials
plt.xlim(timeRangeForLatency)
plt.hold(1)
plt.axvline(respLatency,color='r')

plt.subplot(2,1,2)
plt.plot(interim['timeVec'], interim['avgCount'],'.-k')
plt.hold(1)
plt.axvline(respLatency,color='r')
plt.axhline(interim['threshold'],ls='--',color='0.75')
plt.axhline(interim['baseline'],ls=':',color='0.75')
plt.axhline(interim['maxResponse'],ls=':',color='0.75')
plt.plot(interim['timeVec'],interim['psth'],'r-',mec='none',lw=3)
plt.xlim(timeRangeForLatency)
plt.show()



