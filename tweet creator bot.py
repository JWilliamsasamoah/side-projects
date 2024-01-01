

# # Create a Tweet

# In[16]:


#import all library                      
import os 
import requests
import pandas as pd
from requests_oauthlib import OAuth1Session
import json
from json import dumps, loads, JSONEncoder, JSONDecoder


# In[14]:


def posting():
# while loop 
# tweet variable has to be dictionary 
# other variables by getting the keys and the token you can find your keys and tokens on Twitter api devlopper 
    while True:
        tweet = {"text": input("Enter your tweet!!")}
        bearer_token="ENTER YOUR ON CREDENTIALS  "
        consumer_key = "ENTER YOUR ON CREDENTIALS"
        consumer_secret ="ENTER YOUR ON CREDENTIALS"
        access_token="ENTER YOUR ON CREDENTIALS"
        access_token_secret="ENTER YOUR ON CREDENTIALS"
        
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


        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))


# In[15]:


posting()


# # Verification of the tweet actually posted

# In[8]:


def connect(r):
    bearer_token="ENTER YOUR ON CREDENTIALS"
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    return r


# In[9]:


def request():
    url = "https://api.twitter.com/2/users/1247384276364124161/tweets"
    return requests.request("GET",url,auth=connect).json()


# In[10]:


response= request()
print(response)


# In[11]:


def df_to_see (response):
    return pd.DataFrame(response['data'])


# In[12]:


df= df_to_see(response)
df

