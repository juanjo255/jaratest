from jaratoolbox import loadbehavior
import matplotlib.pyplot as plt
import pandas as pd

def load_data (subject, session):
    paradigm = 'coop4ports' # The paradigm name is also part of the data file name
    behavFile = loadbehavior.path_to_behavior_data(subject,paradigm,session)
    bdata = loadbehavior.BehaviorData(behavFile)
    #print(len(bdata['outcome']))
    return bdata

subject = 'coop014x015'
bdata = load_data(subject, '20230314a')

df = pd.DataFrame({'eventCode':bdata.events['eventCode'],'eventTime':bdata.events['eventTime']})
df.replace(bdata.stateMatrix['eventsNames'], inplace=True)
df_pokes = df[df['eventCode'].isin(['S1in','S2in', "N1in", "N2in"])]
df_pokes['eventCode'].describe()

## PARA JUPYTER

# The first approach will be to compared if a mouse sticks longer to a port if its partner is there too
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import date
from load_behavior_data import collect_events, load_data
#%cd ../..
#%reset -f
#data_1 = load_data("coop010x011", "20230319a")
data_events = collect_events(
        start_subject=(14, 15),
        number_of_mice=1,
        start_date=date(2023, 3, 21),
        end_date=date(2023, 3, 26),
    )
####

# Categorical scatter plot for stage 4 coop014x015
# This to observed if data is enough to start stadistical analysis, not only in quantity, but quality (are they sufficently separated?)
# fig, ax = plt.subplots()
# ax.scatter(x=data["BarrierType"],y=data['Percent reward'],c=(data['BarrierType']=="solid").apply(lambda x:int(x)))
# ax.hlines(y=[int(data.loc[data['BarrierType']=='perforated','Percent reward'].mean()),
#             int(data.loc[data['BarrierType']=='solid','Percent reward'].mean())],xmin=0,xmax=1,colors=['purple','yellow'])

####

data_filt_1 = data_events[
    data_events["Events"]
    .isin(["N1in", "S1in"])
]
data_filt_2 = data_events[
    data_events["Events"]
    .isin(["N2in", "S2in"])
]
data_trials = data_events[
    data_events["Events"]
    .isin(["Forced"])
]
data_trials

#####

# Analyzing the Wait time

+ Here I am trying to determine the time it takes to move from one port to the other one.

+ Of course index have to take into account that sometimes the mice do not go inmediatly to the port
Also, here a doubt arise, The average will change depending on what value I take since sometimes mice are into the task and sometimes they are not.

+ So what value to take?
* Since what I want to know is if the wait time is been enough for the changes between ports, I have to filter the data_1 only to those changes that were equivalent to go from one port to the other one, which are all values equal or lower than 1 sec. since that is the wait time set right now.

#####

data_index_date_1 = data_filt_1.set_index("Date")
data_index_date_2 = data_filt_2.set_index("Date")

mouse1=list()
mouse2=list()
for date in data_index_date_1.index.unique():
    times_curr_date_1 = np.array([])
    times_curr_date_2 = np.array([])
    
    data_1 = data_index_date_1.loc[date].reset_index()
    index_curr_date_1 = list(data_1.index)
    data_2 = data_index_date_2.loc[date].reset_index()
    index_curr_date_2 = list(data_2.index)
    
    for index in index_curr_date_1[:-1]:
        if data_1.loc[index,"Events"] != data_1.loc[index+1,"Events"]:
            times_curr_date_1 = np.append(times_curr_date_1, data_1.loc[index+1,"Event Time"] - data_1.loc[index,'Event Time'])
            
    for index in index_curr_date_2[:-1]:
        if data_2.loc[index,"Events"] != data_2.loc[index+1,"Events"]:
            times_curr_date_2 = np.append(times_curr_date_2, data_2.loc[index+1,"Event Time"] - data_2.loc[index,'Event Time'])

    print("mouse_1: ", times_curr_date_1 [times_curr_date_1<=1].mean())
    print("mouse_2: ", times_curr_date_2 [times_curr_date_2<=1].mean())
    mouse1.append(times_curr_date_1 [times_curr_date_1<=1].mean())
    mouse2.append(times_curr_date_2 [times_curr_date_2<=1].mean())
print(np.mean(mouse1), np.mean(mouse2))