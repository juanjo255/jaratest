import common_init
import utils.load_behavior_data as lbd
import utils.plots_for_analysis as pfa
import matplotlib.pyplot as plt

data = lbd.collect_behavior_data(
    mice_data={
        # "coop014x015": [("2023-07-17", "2023-07-21"), ("2023-07-23", "2023-07-27")],
        # "coop016x017":[("2023-07-10", "2023-07-14"),("2023-07-16", "2023-07-21"),("2023-07-23", "2023-07-27")],
        # 'coop022x023':[('2023-07-17','2023-07-28')],
        ## dark vs dark (perforated_10_mm and transparent_no_holes)
        "coop026x027": [("2023-09-11", "2023-09-20")],
        "coop024x025": [("2023-09-09", "2023-09-17")],
        "coop022x023": [("2023-09-25", "2023-10-06")]
    }
)
data = lbd.correct_data_with_excel(
    fileName="coop_seek_and_find_v2_updated.xlsx",
    sheet_name=data["MiceID"].unique().tolist(),
    data_collected=data,
)

pfa.pct_rewarded_trials(data, colors={'perforated_10_mm':'blue', 'transparent_no_holes':'purple'})
#pfa.rewarded_trials(data)
plt.show()