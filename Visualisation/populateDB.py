from github import Github   # github api access
import json                 # for converting a dictionary to a string
import sqlite3
import os
from collections import defaultdict
g = Github("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")
repoAddress = input("What repo would you like to get? ")
repo =g.get_repo(repoAddress)
issues = repo.get_issues()
labelCountDct = defaultdict(lambda: 0, {})
labelMixMatrix = defaultdict(lambda: defaultdict(lambda: 0, {}) , {}) 
for issue in issues:
       print(issue.get_labels().totalCount)
       if(issue.get_labels().totalCount == 0):
           labelCountDct["unlabeled"] += 1
       for label in issue.get_labels():   
              if issue.get_labels().totalCount>1:
                    for subLabel in issue.get_labels():
                        if subLabel != label:
                            labelMixMatrix[label.name][subLabel.name] += 1
              labelCountDct[label.name] += 1
         

print ("dictionary is " + json.dumps(labelCountDct)+"\n"+json.dumps(labelMixMatrix))

filePath = "Visualisation/data.db"
#Wipes old db if there is one currently at address
if os.path.exists(filePath):
    os.remove(filePath)
# Establish connection
conn = sqlite3.connect(filePath,isolation_level=None)
conn.execute('''CREATE TABLE MAIN
         (LABEL TEXT PRIMARY KEY NOT NULL,
         COUNT          INTEGER NOT NULL,
         NEIGHBOURSBOOL INTEGER NOT NULL);''')
for key in labelCountDct:
    conn.execute('INSERT INTO MAIN (LABEL,COUNT,NEIGHBOURSBOOL)\
            VALUES (:label, :count,:neighboursbool)', {"label":key,"count":labelCountDct[key],
            "neighboursbool":int(key in labelMixMatrix)})
for key in labelMixMatrix:
    conn.execute('''CREATE TABLE {keyString}
         (LABEL TEXT PRIMARY KEY NOT NULL,
         COUNT          INTEGER NOT NULL);'''.format(keyString=key.replace(" ","_")))
    for subkey in labelMixMatrix[key]:
        conn.execute('INSERT INTO {keyString} (LABEL,COUNT)\
            VALUES (:label, :count)'.format(keyString=key.replace(" ","_")), 
            {"label":subkey,"count":labelMixMatrix[key][subkey]})
print("Table created successfully")
conn.close


