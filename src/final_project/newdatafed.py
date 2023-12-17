import os
import sys
from datafed.CommandLib import API
from datafed import version as df_ver

try:
    datapath = os.mkdir("./datapath")
except:
    datapath = "./datapath"

df_api = API()
print("Success! You have DataFed: "+ df_ver)

pl_resp = df_api.projectList()
print(pl_resp)

ls_resp = df_api.collectionItemsList("root", context="p/2023_mem680t")
print(ls_resp)

for record in ls_resp[0].item:
    print(record.id, "\t", record.alias)

import json
parameters = {
    "Title": "Fantasy Football 2023",
    "Description": "Web Scraping ESPN Fantasy Football. All data belongs to ESPN. Offensive players only.",
    "Authors": "Fishhead, ESPN",
    "Affiliations": "ESPN",
    "Date of Data Creation": "September 2023",
    "Data Type": "Numerical",
    "Format": "CSV",
    "Keywords": "Fantasy",
    "Columns": {
        "PLAYER NAME": {"Data Type": "char", "Name, Units": "Player Name"},
        "PLAYER TEAM": {"Data Type": "char", "Name, Units": "Player Team"},
        "PLAYER POSITION": {"Data Type": "char", "Name, Units": "Player Position"},
        "LOC": {"Data Type": "char", "Name, Units": "Location"},
        "OPP": {"Data Type": "char", "Name, Units": "Opponent"},
        "STATUS": {"Data Type": "char", "Name, Units": "Player Status"},
        "PROJ": {"Data Type": "double", "Name, Units": "Projected Points"},
        "PASSING C/A": {"Data Type": "double", "Name, Units": "Passing Completions/Attempts"},
        "PASSING YDS": {"Data Type": "double", "Name, Units": "Passing Yards"},
        "PASSING TD": {"Data Type": "double", "Name, Units": "Passing Touchdowns"},
        "PASSING INT": {"Data Type": "double", "Name, Units": "Passing Interceptions"},
        "RUSHING CAR": {"Data Type": "double", "Name, Units": "Rushing Carries"},
        "RUSHING YDS": {"Data Type": "double", "Name, Units": "Rushing Yards"},
        "RUSHING TD": {"Data Type": "double", "Name, Units": "Rushing Touchdowns"},
        "RECEIVING REC": {"Data Type": "double", "Name, Units": "Receiving Receptions"},
        "RECEIVING YDS": {"Data Type": "double", "Name, Units": "Receiving Yards"},
        "RECEIVING TD": {"Data Type": "double", "Name, Units": "Receiving Touchdowns"},
        "RECEIVING TAR": {"Data Type": "double", "Name, Units": "Receiving Targets"},
        "MISC 2PC": {"Data Type": "double", "Name, Units": "Miscellaneous 2-Point Conversions"},
        "MISC FUML": {"Data Type": "double", "Name, Units": "Miscellaneous Fumbles Lost"},
        "MISC TD": {"Data Type": "double", "Name, Units": "Miscellaneous Touchdowns"},
        "TOTAL": {"Data Type": "double", "Name, Units": "Total Points"},
    }
}

parent_collection = "c/501731761"

dc_resp = df_api.dataCreate(
    "my project data",
    metadata=json.dumps(parameters),
    parent_id=parent_collection,
)
record_id = dc_resp[0].data[0].id
print(record_id)

put_resp = df_api.dataPut(
    record_id,
    r"C:\Users\admin\Desktop\MEMT680\HW4\making_figures\src\making_figures\FantasyFootballWeekly.csv",
    wait=True
)
print(put_resp)