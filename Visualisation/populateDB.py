from github import Github   # github api access
import json                 # for converting a dictionary to a string
import sqlite3
import os
from collections import defaultdict

g = Github("__________________________________________")
repoAddress = input("What repo would you like to get? ")
repo =g.get_repo(repoAddress)
issues = repo.get_issues()
labelCountDct = defaultdict(lambda: 0, {})
labelMixDct = defaultdict(lambda: 0, {})
for issue in issues:
       print(issue.get_labels().totalCount)
       if(issue.get_labels().totalCount == 0):
           labelCountDct["unlabeled"] += 1
       for label in issue.get_labels():   
              if issue.get_labels().totalCount>1:
                    labelMixDct[label.name] += 1
              labelCountDct[label.name] += 1
         

print ("dictionary is " + json.dumps(labelCountDct))


# Establish connection
conn = sqlite3.connect("Visualisation/data.db",isolation_level=None)
conn.execute('''CREATE TABLE MAIN
         (LABEL TEXT PRIMARY KEY NOT NULL,
         COUNT          INTEGER NOT NULL,
         REPEATCOUNT          INTEGER NOT NULL );''')
print("Table created successfully")
for key in labelCountDct:
    conn.execute('INSERT INTO MAIN (LABEL,COUNT,REPEATCOUNT)\
            VALUES (:label, :count, :repeatcount)', {"label":key,"count":labelCountDct[key],"repeatcount":labelMixDct[key]})
conn.close


