"""
Generate a report for each cell, showing ...

N = Noiseburst
T = Tuning curve
A = Ascending
D = Descending
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy import array
from jaratoolbox import settings
from jaratoolbox import celldatabase
from jaratoolbox import behavioranalysis
from jaratoolbox import spikesanalysis
from jaratoolbox import extraplots
from jaratoolbox import ephyscore
from jaratoolbox import spikesorting
import studyparams

dbPath = os.path.join(settings.FIGURES_DATA_PATH, studyparams.STUDY_NAME)
dbFilename = os.path.join(dbPath,'celldb_{}.h5'.format(studyparams.STUDY_NAME))

# -- Load the database of cells --
celldb = celldatabase.load_hdf(dbFilename)

cellDict = {'subject' : 'chad015',
            'date' : '2019-08-08',
            'depth' : 1025,
            'tetrode' : 4,
            'cluster' : 2}

cellInd, dbRow = celldatabase.find_cell(celldb, **cellDict)
oneCell = ephyscore.Cell(dbRow)
timeRange = [-0.1, 0.4]  # In seconds

ax = plt.subplot2grid((4,6), (0,0)) # Subplots
ax0 = plt.subplot2grid((4,6), (0,0))
ax0.axis('off')
plt.text(0.02, 0.8, '{}_{}_{:.0f}um_T{}_c{}'.format(dbRow['subject'], dbRow['date'],
        dbRow['depth'], dbRow['tetrode'], dbRow['cluster']), fontsize=10)
"""
Noiseburst
"""
ephysDataN, bdataN = oneCell.load('noiseburst')
spikeTimesN = ephysDataN['spikeTimes']
eventOnsetTimesN = ephysDataN['events']['stimOn']

(spikeTimesFromEventOnsetN,trialIndexForEachSpikeN,indexLimitsEachTrialN) = \
        spikesanalysis.eventlocked_spiketimes(spikeTimesN, eventOnsetTimesN, timeRange)
"""
-- Noiseburst raster --
"""
ax1 = plt.subplot2grid((4,6), (1,0))
extraplots.raster_plot(spikeTimesFromEventOnsetN,indexLimitsEachTrialN,timeRange)
plt.title('Noiseburst')

"""
-- Noiseburst waveform --
"""
ax2 = plt.subplot2grid((4,6), (2,0))
spikesorting.plot_waveforms(ephysDataN['samples'])
plt.title('Noiseburst')

"""
Tuning Curve
"""
ephysDataT, bdataT = oneCell.load('tc')
spikeTimesT = ephysDataT['spikeTimes']
eventOnsetTimesT = ephysDataT['events']['stimOn']

frequencies_each_trial = bdataT['currentFreq']
array_of_frequencies = np.unique(bdataT['currentFreq'])
trialsEachCondT = behavioranalysis.find_trials_each_type(frequencies_each_trial,array_of_frequencies)

(spikeTimesFromEventOnsetT,trialIndexForEachSpikeT,indexLimitsEachTrialT) = \
        spikesanalysis.eventlocked_spiketimes(spikeTimesT, eventOnsetTimesT, timeRange)

"""
-- Frequency-sorted tuning curve --
"""
ax4 = plt.subplot2grid((4,6), (0,1), rowspan=3)
(pRaster,hcond,zline) = extraplots.raster_plot(spikeTimesFromEventOnsetT,indexLimitsEachTrialT,timeRange, trialsEachCondT)
plt.setp(pRaster,ms=1)
plt.title('Tuning curve')

"""
-- ISI --
"""
ax5 = plt.subplot2grid((4,6), (3,1))
spikesorting.plot_isi_loghist(spikeTimesT)

"""
Three tone - Ascending
"""
ephysDataAscend, bdataAscend = oneCell.load('ascending')
spikeTimesAscend = ephysDataAscend['spikeTimes']
eventOnsetTimesAscend = ephysDataAscend['events']['stimOn']
if len(eventOnsetTimesAscend)==len(bdataAscend['currentFreq'])+1:
    print('Removing last trial from ascending ephys data.')
    eventOnsetTimesAscend = eventOnsetTimesAscend[:-1]
(spikeTimesFromEventOnsetAscend,trialIndexForEachSpikeAscend,indexLimitsEachTrialAscend) = \
                spikesanalysis.eventlocked_spiketimes(spikeTimesAscend, eventOnsetTimesAscend, timeRange)

oddballsAscend = np.flatnonzero(bdataAscend['stimCondition'])

# -- Will need to change this if we ever change the way tones are presented. --
firstOddballAscend = np.array(oddballsAscend[::2])
secondOddballAscend = np.array(oddballsAscend[1::2])
standardForFirstOddballAscend = firstOddballAscend - 2
standardForSecondOddballAscend = secondOddballAscend - 4

firstOddballIndexLimitsAscend = indexLimitsEachTrialAscend[:,firstOddballAscend]
#secondOddballIndexLimitsAscend = indexLimitsEachTrialAscend[:, secondOddballAscend]
# --- Temp ---
print('Remember to change this!')
secondOddballIndexLimitsAscend = indexLimitsEachTrialAscend[:,bdataAscend['currentFreq']==22000]

standardForFirstOddballIndexLimitsAscend = indexLimitsEachTrialAscend[:, standardForFirstOddballAscend]
standardForSecondOddballIndexLimitsAscend = indexLimitsEachTrialAscend[:, standardForSecondOddballAscend]

"""
-- Oddball Trials Raster (first and second) --
"""
ax7 = plt.subplot2grid((4,6), (1,2))
extraplots.raster_plot(spikeTimesFromEventOnsetAscend,firstOddballIndexLimitsAscend,timeRange)
plt.xlabel('Time From Event Onset [s]')
plt.ylabel('Oddball Trial')
plt.title('Ascending - First Oddball')

ax10 = plt.subplot2grid((4,6), (1,3))
extraplots.raster_plot(spikeTimesFromEventOnsetAscend,secondOddballIndexLimitsAscend,timeRange)
plt.xlabel('Time From Event Onset [s]')
plt.ylabel('Oddball Trial')
plt.title('Ascending - Second Oddball')

ax8 = plt.subplot2grid((4,6), (2,2))
ax11 = plt.subplot2grid((4,6), (2,3))
"""
-- Frequency-sorted raster --
"""
frequenciesEachTrialAscend = bdataAscend['currentFreq']
arrayOfFrequenciesAscend = np.unique(bdataAscend['currentFreq'])
labelsForYaxis = ['%.0f' % f for f in arrayOfFrequenciesAscend]

trialsEachCondAscend = behavioranalysis.find_trials_each_type(frequenciesEachTrialAscend,
        arrayOfFrequenciesAscend)

ax6 = plt.subplot2grid((4,6), (0,2))
(pRaster,hcond,zline) = extraplots.raster_plot(spikeTimesFromEventOnsetAscend,indexLimitsEachTrialAscend,timeRange,
        trialsEachCondAscend, labels=labelsForYaxis)
plt.setp(pRaster,ms=1)

"""
-- PSTH --
"""
binWidth = 0.010
timeVec = np.arange(timeRange[0],timeRange[-1],binWidth)
smoothWinSizePsth = 2
lwPsth = 2
downsampleFactorPsth = 1

spikeCountMatFirstOddballAscend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetAscend,
        firstOddballIndexLimitsAscend,timeVec)
spikeCountMatSecondOddballAscend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetAscend,
        secondOddballIndexLimitsAscend,timeVec)
spikeCountMatStdForFirstOddballAscend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetAscend,
        standardForFirstOddballIndexLimitsAscend,timeVec)
spikeCountMatStdForSecondOddballAscend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetAscend,
        standardForSecondOddballIndexLimitsAscend,timeVec)

ax9 = plt.subplot2grid((4,6), (3,2))
extraplots.plot_psth(spikeCountMatFirstOddballAscend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='b',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
extraplots.plot_psth(spikeCountMatStdForFirstOddballAscend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='k',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
plt.xlabel('Time from event onset [s]')
plt.ylabel('Firing Rate [Hz]')
plt.title('Ascending - {} Hz Sound'.format(arrayOfFrequenciesAscend[2]))
# -- Legend for PSTH --
oddball_patch = mpatches.Patch(color='b',label='Oddball')
standard_patch = mpatches.Patch(color='k',label='Standard')
plt.legend(handles=[oddball_patch, standard_patch])

ax12 = plt.subplot2grid((4,6), (3,3))
extraplots.plot_psth(spikeCountMatSecondOddballAscend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='b',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
extraplots.plot_psth(spikeCountMatStdForSecondOddballAscend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='k',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
plt.xlabel('Time from event onset [s]')
plt.ylabel('Firing Rate [Hz]')
plt.title('Ascending - {} Hz Sound'.format(arrayOfFrequenciesAscend[1]))
plt.legend(handles=[oddball_patch, standard_patch])



"""
Three tone - Descending
"""
ephysDataDescend, bdataDescend = oneCell.load('descending')
spikeTimesDescend = ephysDataDescend['spikeTimes']
eventOnsetTimesDescend = ephysDataDescend['events']['stimOn']
if len(eventOnsetTimesDescend)==len(bdataDescend['currentFreq'])+1:
    print('Removing last trial from descending ephys data.')
    eventOnsetTimesDescend = eventOnsetTimesDescend[:-1]

(spikeTimesFromEventOnsetDescend,trialIndexForEachSpikeDescend,indexLimitsEachTrialDescend) = \
                spikesanalysis.eventlocked_spiketimes(spikeTimesDescend, eventOnsetTimesDescend, timeRange)

oddballsDescend = np.flatnonzero(bdataDescend['stimCondition'])

firstOddballDescend = np.array(oddballsDescend[::2])
secondOddballDescend = np.array(oddballsDescend[1::2])
standardForFirstOddballDescend = firstOddballDescend - 2
standardForSecondOddballDescend = secondOddballDescend - 4

firstOddballIndexLimitsDescend = indexLimitsEachTrialDescend[:,firstOddballDescend]
secondOddballIndexLimitsDescend = indexLimitsEachTrialDescend[:, secondOddballDescend]
standardForFirstOddballIndexLimitsDescend = indexLimitsEachTrialDescend[:, standardForFirstOddballDescend]
standardForSecondOddballIndexLimitsDescend = indexLimitsEachTrialDescend[:, standardForSecondOddballDescend]

"""
-- Oddball Trials Raster (first and second) --
"""

ax14 = plt.subplot2grid((4,6), (1,4))
extraplots.raster_plot(spikeTimesFromEventOnsetDescend,firstOddballIndexLimitsDescend,timeRange)
plt.xlabel('Time From Event Onset [s]')
plt.ylabel('Oddball Trial')
plt.title('Descending - First Oddball')

ax17 = plt.subplot2grid((4,6), (1,7))
extraplots.raster_plot(spikeTimesFromEventOnsetDescend,secondOddballIndexLimitsDescend,timeRange)
plt.xlabel('Time From Event Onset [s]')
plt.ylabel('Oddball Trial')
plt.title('Descending - Second Oddball')

ax15 = plt.subplot2grid((4,6), (2,4))
ax18 = plt.subplot2grid((4,6), (2,5))
"""
-- Frequency-sorted raster --
"""
frequenciesEachTrialDescend = bdataDescend['currentFreq']
arrayOfFrequenciesDescend = np.unique(bdataDescend['currentFreq'])
labelsForYaxis = ['%.0f' % f for f in arrayOfFrequenciesDescend]

trialsEachCondDescend = behavioranalysis.find_trials_each_type(frequenciesEachTrialDescend,
        arrayOfFrequenciesDescend)

ax13 = plt.subplot2grid((4,6), (0,4))
(pRaster,hcond,zline) = extraplots.raster_plot(spikeTimesFromEventOnsetDescend,indexLimitsEachTrialDescend,timeRange,
        trialsEachCondDescend, labels=labelsForYaxis)
plt.setp(pRaster,ms=1)

"""
-- PSTH --
"""
binWidth = 0.010
timeVec = np.arange(timeRange[0],timeRange[-1],binWidth)
smoothWinSizePsth = 2
lwPsth = 2
downsampleFactorPsth = 1

spikeCountMatFirstOddballDescend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetDescend,
        firstOddballIndexLimitsDescend,timeVec)
spikeCountMatSecondOddballDescend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetDescend,
        secondOddballIndexLimitsDescend,timeVec)
spikeCountMatStdForFirstOddballDescend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetDescend,
        standardForFirstOddballIndexLimitsDescend,timeVec)
spikeCountMatStdForSecondOddballDescend = spikesanalysis.spiketimes_to_spikecounts(spikeTimesFromEventOnsetDescend,
        standardForSecondOddballIndexLimitsDescend,timeVec)

ax16 = plt.subplot2grid((4,6), (3,4))
extraplots.plot_psth(spikeCountMatFirstOddballDescend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='b',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
extraplots.plot_psth(spikeCountMatStdForFirstOddballDescend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='k',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
plt.xlabel('Time from event onset [s]')
plt.ylabel('Firing Rate [Hz]')
#plt.title('Descending - {} Hz Sound'.format(arrayOfFrequenciesDescend[1]))
# -- Legend for PSTH --
oddball_patch = mpatches.Patch(color='b',label='Oddball')
standard_patch = mpatches.Patch(color='k',label='Standard')
plt.legend(handles=[oddball_patch, standard_patch])

ax19 = plt.subplot2grid((4,6), (3,5))
extraplots.plot_psth(spikeCountMatSecondOddballDescend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='b',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
extraplots.plot_psth(spikeCountMatStdForSecondOddballDescend/binWidth, smoothWinSizePsth,timeVec,trialsEachCond=[],
                colorEachCond='k',linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
plt.xlabel('Time from event onset [s]')
plt.ylabel('Firing Rate [Hz]')
#plt.title('Descending - {} Hz Sound'.format(arrayOfFrequenciesDescend[2]))
plt.legend(handles=[oddball_patch, standard_patch])

"""
-- Last descending waveform --
"""
ax3 = plt.subplot2grid((4,6), (3,0))
spikesorting.plot_waveforms(ephysDataDescend['samples'])
plt.title('Last Descending')

plt.tight_layout()
plt.show()
