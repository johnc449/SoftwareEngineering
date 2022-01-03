from github import Github   # github api access
import json                 # for converting a dictionary to a string
import sqlite3         #for database
import re       #for formatting labels
import os        #for working with files
from collections import defaultdict     #similar to dict but allows us to use default values
g = Github("_______________________") #Put GitHub Key here
repoAddress = input("What repo would you like to get? ")    
repo =g.get_repo(repoAddress)
issues = repo.get_issues()
labelCountDct = defaultdict(lambda: 0, {})  #dict for number of usuages for each label
labelMixMatrix = defaultdict(lambda: defaultdict(lambda: 0, {}) , {})  #dict for labels which are used at same time
for issue in issues:        #iterates over issues
       print(issue.get_labels().totalCount)
       if(issue.get_labels().totalCount == 0):
           labelCountDct["unlabeled"] += 1    #count unlabelled issues
       for label in issue.get_labels():   
              if issue.get_labels().totalCount>1:
                    for subLabel in issue.get_labels():  #counts number of times labels are used 
                        if subLabel != label:        #not the best code but does the job
                            labelMixMatrix[label.name][subLabel.name] += 1
              labelCountDct[label.name] += 1
         

print ("dictionary is " + json.dumps(labelCountDct)+"\n"+json.dumps(labelMixMatrix)) #outputs dictionarys

filePath = "Visualisation/data.db"  #put address of database here   
#Wipes old db if there is one currently at address
if os.path.exists(filePath):
    os.remove(filePath)
# Establish connection
conn = sqlite3.connect(filePath,isolation_level=None)
#creates main tables
conn.execute('''CREATE TABLE MAIN
         (LABEL TEXT PRIMARY KEY NOT NULL,
         COUNT          INTEGER NOT NULL,
         NEIGHBOURSBOOL INTEGER NOT NULL);''')
#fills main table
for key in labelCountDct:
    conn.execute('INSERT INTO MAIN (LABEL,COUNT,NEIGHBOURSBOOL)\
            VALUES (:label, :count,:neighboursbool)', {"label":key,"count":labelCountDct[key],
            "neighboursbool":int(key in labelMixMatrix)})
for key in labelMixMatrix:
    conn.execute('''CREATE TABLE {keyString}
         (LABEL TEXT PRIMARY KEY NOT NULL,
         COUNT          INTEGER NOT NULL);'''.format(keyString=re.sub("[^0-9a-zA-Z]+", "_",key)))
    for subkey in labelMixMatrix[key]:
        conn.execute('INSERT INTO {keyString} (LABEL,COUNT)\
            VALUES (:label, :count)'.format(keyString=re.sub("[^0-9a-zA-Z]+", "_",key)), 
            {"label":subkey,"count":labelMixMatrix[key][subkey]})
print("Table created successfully")
conn.close


