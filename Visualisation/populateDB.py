from github import Github   # github api access
import json                 # for converting a dictionary to a string
import sqlite3
import os

# Load the faker and its providers
from faker import Faker     # for anonymising names
from collections import defaultdict
faker  = Faker()
names  = defaultdict(faker.name)

g = Github("_________________________")

usr = g.get_user()

dct = {'user':         names[usr.login].replace(" ", ""), # anonymising
       'fullname':     names[usr.name],  # anonymising
       'location':     usr.location,
       'company':      usr.company,
       'public_repos': usr.public_repos
       }

print ("dictionary is " + json.dumps(dct))

#not cleaning dictionary currently
#for k, v in dict(dct).items():
#    if v is None:
#        del dct[k]

print ("cleaned dictionary is " + json.dumps(dct))

# Establish connection
conn = sqlite3.connect("Visualisation/data.db")
conn.execute('''CREATE TABLE MAIN
         (USER TEXT PRIMARY KEY NOT NULL,
         FULLNAME          TEXT NOT NULL,
         LOCATION          TEXT,
         COMPANY           TEXT,
         PUBLIC_REPOS      TEXT );''')
print("Table created successfully");
#USER,FULLNAME,LOCATION,COMPANY,PUBLIC_REPOS
conn.execute("INSERT INTO COMPANY (USER,FULLNAME,LOCATION,COMPANY,PUBLIC_REPOS) \ #fix this, wrong format
      VALUES ("+str(dct["user"])+","+str(dct["fullname"])+","+
      str(dct["location"])+","+ str(dct["company"])+","+ str(dct["public_repos"])+")")

'''
# and for each of them we'll get and add a count of the number of repos they have
fc = usr.followers
print ("followers: " + str(fc))

# now lets get those followers
fl = usr.get_followers()

for f in fl:
    dct = {'user':         names[f.login].replace(" ",""), # anonymising
           'fullname':     names[f.name], # anonymising
           'location':     f.location,
           'company':      f.company,
           'public_repos': f.public_repos
           }
    for k, v in dict(dct).items():
        if v is None:
            del dct[k]
        
    print("follower: " + json.dumps(dct))
    conn.execute("INSERT INTO main VALUES (?,?,?,?,?)",
     [dct["user"], dct["fullname"], dct["location"],dct["company"],dct["public_repos"]]) 

'''


