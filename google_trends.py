from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd

pytrends = TrendReq(hl='en-US')


keywords = (input('Input elements with comma to seprate(Max 5): ').split(','))
print(keywords)

pytrends.build_payload(keywords, timeframe='all')

data = pytrends.interest_over_time()


data = pd.DataFrame(data)
data.plot()
plt.title('google trends')
plt.xlabel('Years')
plt.ylabel('Weekly searches')
plt.legend(keywords, loc='upper left')


pytrends.build_payload(keywords, timeframe='today 5-y')

data = pytrends.interest_over_time()


data = pd.DataFrame(data)
data.plot()
plt.title('google trends')
plt.xlabel('Years')
plt.ylabel('Weekly searches')
plt.legend(keywords, loc='upper left')

plt.show()