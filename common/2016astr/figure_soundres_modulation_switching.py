'''
Create figure about the activity of astr neurons during sound being modulated by contingency in the switching task.
'''
import os
import numpy as np
from matplotlib import pyplot as plt
from jaratoolbox import colorpalette as cp
from jaratoolbox import extraplots
from jaratoolbox import settings
import matplotlib.gridspec as gridspec
import matplotlib
import figparams
import matplotlib.patches as mpatches


removedDuplicates = True

matplotlib.rcParams['font.family'] = 'Helvetica'
matplotlib.rcParams['svg.fonttype'] = 'none'  # To

dataDir = os.path.join(settings.FIGURESDATA, figparams.STUDY_NAME)

SAVE_FIGURE = 1
outputDir = '/tmp/'
if removedDuplicates:
    figFilename = 'fig_modulation_switching_remove_dup' # Do not include extension
else:
    figFilename = 'fig_modulation_switching'

figFormat = 'pdf' # 'pdf' or 'svg'
figSize = [8,6]

fontSizeLabels = figparams.fontSizeLabels
fontSizeTicks = figparams.fontSizeTicks
fontSizePanel = figparams.fontSizePanel

timeRangeSound = [-0.2, 0.4]
msRaster = 2
smoothWinSizePsth = 3
lwPsth = 2
downsampleFactorPsth = 1

#colormapSound =  

labelPosX = [0.07, 0.46]   # Horiz position for panel labels
labelPosY = [0.9, 0.45]    # Vert position for panel labels

#COLORMAP = {'leftTrials':'red', 'rightTrials':'green'}

fig = plt.gcf()
fig.clf()
fig.set_facecolor('w')

gs = gridspec.GridSpec(4, 4)
gs.update(left=0.15, right=0.85, wspace=1, hspace=1)


# -- Panel A: schematic of switching task-- #
ax1 = plt.subplot(gs[0:2, 0:2])
plt.axis('off')
ax1.annotate('A', xy=(labelPosX[0],labelPosY[0]), xycoords='figure fraction', fontsize=fontSizePanel, fontweight='bold')


# -- Panel B: representative sound-evoked raster from switching task, Modulated-- #
ax2 = plt.subplot(gs[0, 2:4])

rasterFilename = 'example_switching_midfreq_soundaligned_raster_test089_20160124a_T4_c6.npz' 
rasterFullPath = os.path.join(dataDir, rasterFilename)
rasterExample =np.load(rasterFullPath)

trialsEachCond = rasterExample['trialsEachCond']
colorEachCond = rasterExample['colorEachCond']
spikeTimesFromEventOnset = rasterExample['spikeTimesFromEventOnset']
indexLimitsEachTrial = rasterExample['indexLimitsEachTrial']
timeRange = rasterExample['timeRange']

pRaster, hcond, zline = extraplots.raster_plot(spikeTimesFromEventOnset,
                                               indexLimitsEachTrial,
                                               timeRange=timeRangeSound,
                                               trialsEachCond=trialsEachCond,
                                               colorEachCond=colorEachCond)

plt.setp(pRaster, ms=msRaster)
plt.xlabel('Time from sound onset (s)',fontsize=fontSizeLabels) 
plt.ylabel('Trials',fontsize=fontSizeLabels)
#plt.xlim(timeRangeSound[0],timeRangeSound[1])
ax2.annotate('B', xy=(labelPosX[1],labelPosY[0]), xycoords='figure fraction', fontsize=fontSizePanel, fontweight='bold')


# -- Panel B2: representative sound-evoked psth from switching task, Modulated -- #
ax3 = plt.subplot(gs[1, 2:4])

psthFilename = 'example_switching_midfreq_soundaligned_psth_test089_20160124a_T4_c6.npz' 
psthFullPath = os.path.join(dataDir, psthFilename)
psthExample =np.load(psthFullPath)

trialsEachCond = psthExample['trialsEachCond']
colorEachCond = psthExample['colorEachCond']
spikeCountMat = psthExample['spikeCountMat']
timeVec = psthExample['timeVec']
binWidth = psthExample['binWidth']
timeRange = psthExample['timeRange']

extraplots.plot_psth(spikeCountMat/binWidth,smoothWinSizePsth,timeVec,trialsEachCond=trialsEachCond,colorEachCond=colorEachCond,linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)
extraplots.set_ticks_fontsize(plt.gca(),fontSizeTicks)
plt.axvline(x=0,linewidth=1, color='darkgrey')
plt.xlim(timeRangeSound[0],timeRangeSound[1])
plt.xlabel('Time from sound onset (s)',fontsize=fontSizeLabels)
plt.ylabel('Firing rate (spk/sec)',fontsize=fontSizeLabels)


# -- Panel C: representative sound-evoked raster from switching task, Not modulated -- #
ax4 = plt.subplot(gs[2, 0:2])

rasterFilename = 'example_switching_midfreq_soundaligned_raster_adap020_20160524a_T2_c9.npz' 
rasterFullPath = os.path.join(dataDir, rasterFilename)
rasterExample =np.load(rasterFullPath)

trialsEachCond = rasterExample['trialsEachCond']
colorEachCond = rasterExample['colorEachCond']
spikeTimesFromEventOnset = rasterExample['spikeTimesFromEventOnset']
indexLimitsEachTrial = rasterExample['indexLimitsEachTrial']
timeRange = rasterExample['timeRange']

pRaster, hcond, zline = extraplots.raster_plot(spikeTimesFromEventOnset,
                                               indexLimitsEachTrial,
                                               timeRange=timeRangeSound,
                                               trialsEachCond=trialsEachCond,
                                               colorEachCond=colorEachCond,
                                               fillWidth=None,labels=None)

plt.setp(pRaster, ms=msRaster)
plt.xlabel('Time from sound onset (s)',fontsize=fontSizeLabels)
plt.ylabel('Trials',fontsize=fontSizeLabels)
#plt.xlim(timeRangeSound[0],timeRangeSound[1])
ax4.annotate('C', xy=(labelPosX[0],labelPosY[1]), xycoords='figure fraction', fontsize=fontSizePanel, fontweight='bold')


# -- Panel C2: representative sound-evoked psth from switching task, Not modulated -- #
ax5 = plt.subplot(gs[3, 0:2])

psthFilename = 'example_switching_midfreq_soundaligned_psth_adap020_20160524a_T2_c9.npz' 
psthFullPath = os.path.join(dataDir, psthFilename)
psthExample =np.load(psthFullPath)

trialsEachCond = psthExample['trialsEachCond']
colorEachCond = psthExample['colorEachCond']
spikeCountMat = psthExample['spikeCountMat']
timeVec = psthExample['timeVec']
binWidth = psthExample['binWidth']
timeRange = psthExample['timeRange']

extraplots.plot_psth(spikeCountMat/binWidth,smoothWinSizePsth,timeVec,trialsEachCond=trialsEachCond,colorEachCond=colorEachCond,linestyle=None,linewidth=lwPsth,downsamplefactor=downsampleFactorPsth)

#plt.legend()
extraplots.set_ticks_fontsize(plt.gca(),fontSizeTicks)
plt.axvline(x=0,linewidth=1, color='darkgrey')
plt.xlim(timeRangeSound[0],timeRangeSound[1])
plt.xlabel('Time from sound onset (s)',fontsize=fontSizeLabels)
plt.ylabel('Firing rate (spk/sec)',fontsize=fontSizeLabels)


# -- Panel D: summary distribution of switching modulation index -- #
ax6 = plt.subplot(gs[2:,2:4])

if removedDuplicates:
    summaryFilename = 'summary_switching_sound_modulation_good_cells_responsive_midfreq_remove_dup.npz'
else:
    summaryFilename = 'summary_switching_sound_modulation_good_cells_responsive_midfreq.npz'
summaryFullPath = os.path.join(dataDir,summaryFilename)
summary = np.load(summaryFullPath)

sigModulated = summary['modulated']
sigMI = summary['modulationIndex'][sigModulated]
nonsigMI = summary['modulationIndex'][~sigModulated]
plt.hist([sigMI,nonsigMI], bins=50, color=['k','darkgrey'], edgecolor='None', stacked=True)

sig_patch = mpatches.Patch(color='k', label='Modulated')
nonsig_patch = mpatches.Patch(color='darkgrey', label='Not modulated')
plt.legend(handles=[sig_patch,nonsig_patch], fontsize=fontSizeTicks, frameon=False, labelspacing=0.1, handlelength=0.2)

plt.axvline(x=0, linestyle='--',linewidth=1.5, color='k')
extraplots.set_ticks_fontsize(plt.gca(),fontSizeTicks)
plt.xlabel('Modulation index', fontsize=fontSizeLabels)
plt.ylabel('Number of cells', fontsize=fontSizeLabels)

ax6.annotate('D', xy=(labelPosX[1],labelPosY[1]), xycoords='figure fraction', fontsize=fontSizePanel, fontweight='bold')

plt.show()

if SAVE_FIGURE:
    extraplots.save_figure(figFilename, figFormat, figSize, outputDir)

