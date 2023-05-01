salineHighFreq = {
    "runStart": ["2:13", "4:58"],
    "runStop": ["2:25", "5:00"]
}

salineLowFreq = {
    "runStart": ["0:00", "0:21", "1:04"],
    "runStop": ["0:12", "0:38", "1:23"]
}

salineFMDown = {
    "runStart": ["1:08", "1:30", "5:46"],
    "runStop": ["1:24", "1:49", "5:51"]
}

salineFMUp = {
    "runStart": ["1:54", "2:25", "3:45", "4:06"],
    "runStop": ["2:22", "2:45", "4:00", "4:20"]
}

doiHighFreq = {
    "runStart": ["0:00", "0:10", "0:24", "0:29", "0:52", "1:42", "1:56", "2:05", "2:25", "3:57", "4:53"],
    "runStop": ["0:04", "0:19", "0:25", "0:50", "1:33", "1:50", "1:58", "2:20", "3:52", "4:38", "4:57"]
}

doiLowFreq = {
    "runStart": ["0:00", "0:18", "0:51", "1:26", "1:33", "1:45", "1:50", "2:41", "2:47", "3:10", "3:25", "3:47", "4:03", "4:17"],
    "runStop": ["0:15", "0:44", "1:00", "1:27", "1:42", "1:48", "2:38", "2:44", "3:07", "3:17", "3:41", "4:00", "4:13", "5:00"]
}

doiFMDown = {
    "runStart": ["0:00", "1:06", "1:40", "1:59", "2:15", "4:59"],
    "runStop": ["1:02", "1:36", "1:51", "2:11", "4:54", "5:50"]
}

doiFMUp = {
    "runStart": ["0:00", "0:13", "0:26", "1:22", "3:51", "4:06", "4:25", "4:31", "4:35", "4:45", "4:54", "5:01", "5:47"],
    "runStop": ["0:07", "0:20", "1:17", "3:48", "4:03", "4:21", "4:30", "4:32", "4:42", "4:52", "4:55", "5:42", "5:50"]
}


'''
Potential for adding multiple days later with nested dictionaries

salineFreq = {
    "2022-01-01": {
        "runStart": ["2:13", "4:58"],
        "runStop": ["2:25", "5:00"]
    },
    "2022-01-02": {
        "runStart": ["3:13", "6:58"],
        "runStop": ["3:25", "6:00"]
    },
    "2022-01-03": {
        "runStart": ["1:13", "2:58"],
        "runStop": ["1:25", "3:00"]
    }
}


accessing later would look like:

date = "2022-01-01"
salineHighFreq = salineFreq[date]

or make the date the outside dictionary 

'''


