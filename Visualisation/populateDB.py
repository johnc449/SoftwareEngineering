from github import Github   # github api access
import json                 # for converting a dictionary to a string
import pymongo              # for mongodb access
import os

#Access Token- Keep this out of the way
g = Github("--------------------------")

#Let's get the user object and build a data dictionary
usr = g.get_user()

dct = {'user':         names[usr.login].replace(" ", ""), # anonymising
       'fullname':     names[usr.name],  # anonymising
       'location':     usr.location,
       'company':      usr.company,
       'public_repos': usr.public_repos
       }

print ("dictionary is " + json.dumps(dct))





