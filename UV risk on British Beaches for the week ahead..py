
# coding: utf-8

# In[1]:


import json
from pprint import pprint
import urllib.request
import re
import datetime


# In[2]:


url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=3f7c1013-95ee-48ce-b8b1-bc5a8932a350'


# In[3]:


req = urllib.request.Request(url = url)


# In[4]:


go = urllib.request.urlopen(req)


# In[5]:


r = go.read().decode('utf-8')


# In[6]:


rd = json.loads(r)


# In[7]:


beachlocations = {}

for i in rd['Locations']['Location']:
    if 'Beach' in i['name']:
        beachlocations[i['name']] = i['id']


# In[8]:


beach_id = list(beachlocations.values())


# In[13]:


type(beach_id)


# In[9]:


listofurls = []

for ids in beachlocations.values():
    l = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/{a}?res=daily&key=4e38a9ec-5654-417b-9e43-afa4873e6416'.format(a=ids)
    listofurls.append(l)


# In[10]:


listofurls[1]


# In[289]:


pprint(beachlocations)


# In[11]:


url2=listofurls[0]
req2 = urllib.request.Request(url = url2)
go2 = urllib.request.urlopen(req2)
r2 = go2.read().decode('utf-8')
rd2 = json.loads(r2)


# In[13]:


name = []
uv = []
i_d = []
date = []

for url2 in listofurls:
    req2 = urllib.request.Request(url = url2)
    go2 = urllib.request.urlopen(req2)
    r2 = go2.read().decode('utf-8')
    rd2 = json.loads(r2)
    
    for i in range(5):
        uv.append(rd2['SiteRep']['DV']['Location']['Period'][i]['Rep'][0]['U'])
        name.append(rd2['SiteRep']['DV']['Location']['name'])
        date.append(rd2['SiteRep']['DV']['Location']['Period'][i]['value'][0:10])
        i_d.append(rd2['SiteRep']['DV']['Location']['i'])

#print(name)        
z = zip(i_d, name, date, uv)
for i in z:
    print(i)


# In[288]:


import pickle 
with open(r'C:\python_projects\pickles\uvtask.pkl', 'wb') as pkl:   #name of the pickle is objs. wb = write binary(not readable by human)
    pickle.dump(i, pkl)

