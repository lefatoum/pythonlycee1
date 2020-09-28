import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.AU.PXP_IX.?startPeriod=1957&endPeriod=2019'

data = requests.get(url).json()

auxp = pd.DataFrame(data['CompactData']['DataSet']['Series']['Obs'])
print(auxp)

# Rename columns
auxp.columns = ['date','auxp']

# Convert price index series as a float
auxp['auxp'] = auxp.auxp.astype(float)

#get a fix frequency dataindex. We have quarterly data, therefore, we take as start period the first date and last value the number of rows and define 3M as the frequency

frequency = pd.date_range(pd.to_datetime(auxp.date[0]), periods=len(auxp.index), freq='3M')

#Set our new frequency data index as index of dataframe
auxp = auxp.set_index(pd.DatetimeIndex(frequency))


auxp['auxp'].plot(grid=True, figsize=(9, 5), color="orange", linewidth=2,)
plt.ylabel('Index')
plt.xlabel('Year')
plt.title('Australia: Export Price Index ')
plt.show()