# read the data
# ask for user input (what instrument, what econ indicator, direction of surprise, magnitude of surprise)
# clean data: positive, no surprise or negative + calculate magnitude + adjust for time diff?
# go into data, find econ indicator
# filter data: according to request
# output: find date

from datetime import datetime
import pandas as pd
df = pd.read_csv('DummyData.csv')
#have to use filepath instead of file name

df['Date']=pd.to_datetime(df['Date'], format='%m/%d/%Y')

for x in df['Time']:
   x = datetime.strptime(x, "%H:%M")
   time_obj = x.time()

print(df)

class user_input:
    def __init__(self, instrument, indicator, surprise_sign_input, surprise_magnitude):
        self.instrument = instrument  # to link to drop down
        self.indicator = indicator  # to link to autofill
        self.surprise_sign_input = surprise_sign_input  # to link to drop down (exceed, meet, below expections)
        self.surprise_magnitude = surprise_magnitude  # to link to drop down (large, medium, small), if user chooses 'meet', cannot choose magnitude
john=user_input("Apple","ISM Maunfacturing","Exceed","Small")

def surprise_sign_calc(row):
  if row['Actual']-row['Median Est']>0:
      return('Exceed')
  elif row['Actual']-row['Median Est']<0:
      return('Below')
  else:
      return('Meet')

df['surprise_sign']=df.apply(surprise_sign_calc, axis=1) #create new row for surprise sign

def surprise_magnitude_calc(row):
  if abs((row['Actual']-row['Median Est'])/row['SD'])>2:
      return('Large')
  elif abs((row['Actual']-row['Median Est'])/row['SD'])<1:
      return('Small')
  else:
      return('Medium')

df['surprise_magnitude']=df.apply(surprise_magnitude_calc, axis=1) #creates new row for surprise magnitude

#print(df)

if john.surprise_sign_input != "Meet":
    df_results=df[df['Event'].str.contains(john.indicator)& df['surprise_sign'].str.contains(john.surprise_sign_input)&
              df['surprise_magnitude'].str.contains(john.surprise_magnitude)]
else:
    df_results=df[df['Event'].str.contains(john.indicator)& df['surprise_sign'].str.contains(john.surprise_sign_input)]

list_of_results = df_results['Date']
print(list_of_results)

df_instrument = pd.read_csv('aapl.csv')

df_instrument.iloc[:,0]=pd.to_datetime(df_instrument.iloc[:,0], format='%Y-%m-%d') #for some reason cannot use df_instrument.columns[0] here

#set date column as index
df_instrument.set_index(df_instrument.columns[0], inplace=True)

print(df_instrument)

#match results with index of the row
for shortlisted_date in list_of_results:
    df_output = df_instrument.loc[[shortlisted_date]]

print(df_output)