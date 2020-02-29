#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.io import output_notebook


# In[35]:


earnings=pd.read_csv("TeslaEarnings.csv", index_col=7)
sp=pd.read_csv("TeslaStockPrice.csv", index_col = 0)


# In[36]:


stringslist=[]
for i in earnings["Ann Date"]:
    stringslist.append(i.split("/")) 
for j in stringslist:
    if j[0] == "11":
        continue
    elif j[0]=="10":
        continue
    elif j[0] == "12":
        continue
    elif j[0][0] != "0":
        j[0]="0"+j[0]
seperator= "/"  
cleanedlist=[]
for j in stringslist:
    cleanedlist.append(seperator.join(j))


earnings["Ann Date"]=cleanedlist


# In[37]:


earnings_dict={}
for j in earnings["Ann Date"]:
    pass
for i in earnings.index:
    if type(i)==str and i !="N.M.":
        earnings_dict[float(i)]=earnings.at[i,"Ann Date"]
    elif i == "N.M.":
        continue
    else:
        continue
for i in earnings_dict:
    try:
           earnings_dict[i]=dt.strptime(earnings_dict[i],"%m/%d/%Y")
    except TypeError:
        continue
earnings_dict        


# In[38]:


prices=sp["Last Price"]


# In[39]:


prices_dict={}
for i in prices.index:
    prices_dict[dt.strptime(i, "%m/%d/%Y")]=float(prices[i])


# In[40]:



x=float(0.3)
for i in earnings_dict.keys():
    if abs(i-x) <= 0.5:
        try:
            if i-x <=0:
                print(earnings_dict[i], " ",prices_dict[earnings_dict[i]]," ", "Has a lower value than requested", " ", i)
            elif i-x > 0:
                 print(earnings_dict[i], " ",prices_dict[earnings_dict[i]]," ", "Has a higher value than requested", " ", i)
        except TypeError:
            continue
#The -0.1111 is a real problem. What do I do if the same value appears twice for 2 different dates.... earnings dict is the one with the problem
#(prices_dict(earnings_dict[i]+timedelta(days=1))-prices_dict(earnings_dict[i]))/prices_dict(earnings_dict[i])


# In[41]:


'''x=float(input("Please input your surprise value\n"))

for i in earnings_dict.keys():
    if abs(i-x) <= 0.5:
        try:
            if i-x <=0:
                try:
                    print("For ", earnings_dict[i], "\n","The one day price change after earnings is"," ",(prices_dict[earnings_dict[i]+timedelta(days=1)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n","The 20 day price change after earnings is", " ", (prices_dict[earnings_dict[i]+timedelta(days=20)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n", "The 100 day change after earnings is", " ",(prices_dict[earnings_dict[i]+timedelta(days=100)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n", "The actual surprise ",i,"  has a lower value than requested","\n")
                except KeyError:
                    try:
                        print("For ", earnings_dict[i], "\n","The one day price change after earnings is"," ",(prices_dict[earnings_dict[i]+timedelta(days=1)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n","The 20 day price change after earnings is", " ", (prices_dict[earnings_dict[i]+timedelta(days=20)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n", "The actual surprise ",i,"  has a lower value than requested","\n")
                    except KeyError:
                        try:
                            print("For ", earnings_dict[i], "\n","The one day price change after earnings is"," ",(prices_dict[earnings_dict[i]+timedelta(days=1)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n","The actual surprise ",i,"  has a lower value than requested","\n")
                        except KeyError:
                            continue                          
            elif i-x > 0:
                try:
                    print("For ", earnings_dict[i], "\n","The one day price change after earnings is"," ",(prices_dict[earnings_dict[i]+timedelta(days=1)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n","The 20 day price change after earnings is", " ", (prices_dict[earnings_dict[i]+timedelta(days=20)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n", "The 100 day change after earnings is", " ",(prices_dict[earnings_dict[i]+timedelta(days=100)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n", "The actual surprise ",i,"  has a higher value than requested","\n")
                except KeyError:
                    try:
                        print("For ", earnings_dict[i], "\n","The one day price change after earnings is"," ",(prices_dict[earnings_dict[i]+timedelta(days=1)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n","The 20 day price change after earnings is", " ", (prices_dict[earnings_dict[i]+timedelta(days=20)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n", "The actual surprise ",i,"  has a higher value than requested","\n")
                    except KeyError:
                        try:
                            print("For ", earnings_dict[i], "\n","The one day price change after earnings is"," ",(prices_dict[earnings_dict[i]+timedelta(days=1)]-prices_dict[earnings_dict[i]])/prices_dict[earnings_dict[i]],"\n","The actual surprise ",i,"  has a higher value than requested","\n")
                        except KeyError:
                            continue      
        except TypeError:
            continue
else:
    print("")'''


# In[42]:


unneeded_data=['Per', 'Per End', 'C', 'Reported',
       'Guidance', '%Guid Surp', '%Px Chg', 'T12M', 'P/E']
earnings.drop(unneeded_data,inplace=True,axis=1)


# In[43]:


earnings["surprisevalues"]=earnings.index


# In[44]:


len(earnings)        
i=0
list=[]
while i < len(earnings):
    list.append(i)
    i+=1
print(list) 
earnings.index=list

   


# In[45]:


earnings.index=earnings["surprisevalues"] 


# In[46]:


sv=earnings["surprisevalues"]
nm=sv.str.contains("N.M.")
earnings["surprisevalues"]=np.where(nm,None,sv.str.replace(" ","-"))
#earnings["surprisevalues"].fillna(mean,inplace=True)
list=[]
for i in earnings["surprisevalues"]:
    try:
        list.append(float(i))
    except TypeError:
        list.append(i)


# In[47]:


earnings["surprisevalues"]=list


# In[48]:


list2=[]
for i in list:
    if type(i)==float:
        list2.append(i)
mean=float(sum(list2)/len(list2))
array2=np.array(list2)
sd=float(np.std(array2))


# In[49]:


zlist=[]
zlist2=[]
for i in earnings["surprisevalues"]:
    zlist.append(i)
for i in zlist:
    zlist2.append((i-mean)/sd)


# In[50]:


earnings["z"]=zlist2


# In[51]:


surplist=[]
for i in zlist2:
        if abs(i) >0:
            if abs(i) <=1:
                surplist.append("small")
            elif abs(i)>1: 
                if abs(i)<=2:
                    surplist.append("medium")
                elif abs(i)>2:
                    surplist.append("large")
        else:
            surplist.append(None)


# In[52]:


dirlist=[]
for i in zlist2:
    if i>0:
        dirlist.append("positive")
    elif i<0:
        dirlist.append("negative")
    elif i==0:
        dirlist.append("No surprise")
    else:
        dirlist.append(None)


# In[53]:


earnings["direction"]=dirlist


# In[54]:


earnings["surprisemagnitude"]=surplist


# In[55]:


list4=[]
i=0
while i<len(earnings):
    list4.append(i)
    i+=1


# In[56]:


earnings.index=list4


# In[57]:


earnings=earnings.drop(earnings.index[0])


# In[58]:


list5=[]
i=0
while i<len(earnings):
    list5.append(i)
    i+=1


# In[59]:


earnings.index=list5


# In[60]:


dates=[]
dates2=[]
for i in earnings["Ann Date"]:
    dates.append(i)
for i in dates:
    dates2.append(dt.strptime(i,"%m/%d/%Y"))
earnings["Ann Date"]=dates2    


# In[61]:


for i in earnings.index:
    if earnings.loc[i]["Actual"] >0 and earnings.loc[i]["Estimate"]<0:
        earnings.at[i,"direction"]="positive"
        earnings.at[i,"surprisemagnitude"]="huge"
    elif earnings.loc[i]["Actual"]<0 and earnings.loc[i]["Estimate"]>0:
        earnings.at[i,"direction"]="negative"
        earnings.at[i,"surprisemagnitude"]="huge"


# In[62]:


'''for i in earnings.index:
     if earnings.iloc[i]["direction"]=="positive":
            print(earnings.iloc[i]["Ann Date"])'''


# In[63]:


spdate=[]
spdate2=[]
for i in sp.index:
    spdate.append(i)
for i in spdate:
    spdate2.append(dt.strptime(i,"%m/%d/%Y"))
    


# In[64]:


sp.index=spdate2


# In[65]:


direc=input("positive or negative?")
mag=input("small, medium, large or huge?")
for i in earnings.index:
    if earnings.iloc[i]["direction"]==direc and earnings.iloc[i]["surprisemagnitude"]==mag:
        try:
            print("On",earnings.loc[i]["Ann Date"],"\n The one day price change was",sp.at[(earnings.loc[i]["Ann Date"]+timedelta(days=1)),"Last Price"]-sp.at[earnings.loc[i]["Ann Date"],"Last Price"],"\n The 20 day price change was",sp.at[(earnings.loc[i]["Ann Date"]+timedelta(days=20)), "Last Price"]-sp.at[earnings.loc[i]["Ann Date"], "Last Price"],"\n And the 100 day price change was",sp.at[(earnings.loc[i]["Ann Date"]+timedelta(days=100)), "Last Price"]-sp.at[earnings.loc[i]["Ann Date"], "Last Price"],"\n")
        except KeyError:
            try:
                print("On",earnings.loc[i]["Ann Date"],"\n The one day price change was",sp.at[(earnings.loc[i]["Ann Date"]+timedelta(days=1)),"Last Price"]-sp.at[earnings.loc[i]["Ann Date"],"Last Price"],"\n And the 20 day price change was",sp.at[(earnings.loc[i]["Ann Date"]+timedelta(days=50)), "Last Price"]-sp.at[earnings.loc[i]["Ann Date"], "Last Price"],"\n")
            except KeyError:
                print("On",earnings.loc[i]["Ann Date"],"\n The one day price change was",sp.at[(earnings.loc[i]["Ann Date"]+timedelta(days=1)),"Last Price"]-sp.at[earnings.loc[i]["Ann Date"],"Last Price"],"\n")


# In[ ]:





# In[ ]:




