#!/usr/bin/env python
# coding: utf-8

# In[211]:


import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import cv2
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import time
import os
import warnings
warnings.filterwarnings("ignore")
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json-patch+json',
}

data = '{ "Username": "REPLACE", "Password": "REPLACE" }'

response = requests.post('https://nhl-east-rest.oasis.smt.com/optics3d/v2.80/auth/login', headers=headers, data=data)



token = response.json()['token']


# In[212]:


def connect(r):
    r.headers["Authorization"] = f"Bearer {token}"
    return r


# In[219]:


confDict = {'NJD':'EAST',
            'NYI':'EAST',
            'NYR':'EAST',
            'PHI':'EAST',
            'PIT':'EAST',
            'BOS':'EAST',
            'BUF':'EAST',
            'MTL':'EAST',
            'OTT':'EAST',
            'TOR':'EAST',
            'CAR':'EAST',
            'FLA':'EAST',
            'TBL':'EAST',
            'WSH':'EAST',
            'CHI':'WEST',
            'DET':'EAST',
            'NSH':'WEST',
            'STL':'WEST',
            'CGY':'WEST',
            'COL':'WEST',
            'EDM':'WEST',
            'VAN':'WEST',
            'ANA':'WEST',
            'DAL':'WEST',
            'LAK':'WEST',
            'SJS':'WEST',
            'CBJ':'EAST',
            'MIN':'WEST',
            'WPG':'WEST',
            'ARI':'WEST',
            'VGK':'WEST',
            'SEA':'WEST'
            }

def getGameID(date,homeTeam,awayTeam):
    
    searchString = date+"_"+awayTeam+"@"+homeTeam
    
    url = f'https://nhl-east-rest.oasis.smt.com/optics3d/v3.00/GameSchedule?Year=2021'
    response = requests.get(url, auth=connect)
    print(response)
    trackingData = response.json()
 
    for i in range (0,len(trackingData[0]['Events'])):
        if trackingData[0]['Events'][i]['EventId'].find(searchString)>0:
            return trackingData[0]['Events'][i]['EventId'],trackingData[0]['Events'][i]['ActualStartUTC'],trackingData[0]['Events'][i]['ActualEndUTC']
    raise ValueError('Could not find a gameID. Possible date or order of Home/Away is wrong')


# In[220]:


#Set Date in format YYYY_MM_DD
#Define Home and Away
date = '2022_05_02'
homeTeam = 'TOR'
awayTeam = 'TBL'
conf = confDict[homeTeam]

gameID,gameStartUTC,gameEndUTC = getGameID(date,homeTeam,awayTeam)


print(gameID)


# In[204]:



    url = f'https://nhl-{confDict[homeTeam]}-rest.oasis.smt.com/optics3d/v2.80/MarkerActivity?Game={gameID}&MinorType=EventShot'

    response = requests.get(url, auth=connect) 
    print(response)
    scoreboardData = response.json()
    scoreboardData = pd.json_normalize(scoreboardData)
    #pd.set_option("max_rows", None)
    


# In[154]:


import os 
import requests
import pandas as pd
from requests_oauthlib import OAuth1Session
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import time
from datetime import datetime


# In[209]:


def posting():
# while loop 
# tweet variable has to be dictionary 
# other variables by getting the keys and the token you can find your keys and tokens on Twitter api devlopper 
  while True:
        
        url = f'https://nhl-{confDict[homeTeam]}-rest.oasis.smt.com/optics3d/v2.80/MarkerActivity?Game={gameID}&MinorType=EventShot'
        

        response = requests.get(url, auth=connect) 
        print(response)
        scoreboardData = response.json()
        scoreboardData = pd.json_normalize(scoreboardData)
        pd.set_option("max_rows", None)
        SA=scoreboardData[scoreboardData['Descriptor_'].str.contains('Shot Attempt')]
        HITS=scoreboardData[scoreboardData['Descriptor_'].str.contains('HITS')]
        print(SA['Descriptor_'].tail(1))
        tweet = {"text":SA['Descriptor_'].iloc[-1]}
        bearer_token="REPLACE"
        consumer_key = "REPLACE"
        consumer_secret ="REPLACE"
        access_token="REPLACE"
        access_token_secret="REPLACE"
        
#Making the request of the authentication v1 and connecting everything       
        oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    
        )
# the response(output)
# response = 200 = valid response(it tweeted)
# response =403 = account unable to process this request 
#response=401= broken url or invalid keys,Token or tweet duplication 
# To get the url you can use postman!
        response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=tweet,
        )

        time.sleep(3)
        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))
posting()


# In[222]:





# In[ ]:




