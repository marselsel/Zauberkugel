import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("AAPL.csv")

# Sort DataFrame by date
df = df.sort_values('Date')

plt.figure(figsize = (18,9))
plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Mid Price',fontsize=18)

plt.show()