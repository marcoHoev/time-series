from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel('data/QualidadeARO3.xlsx')
data.head()

plt.figure(figsize=[15, 7.5]); # Set dimensions for figure
plt.plot(data)
plt.title('time series of hourly-ground-levels of O3 values, in micrograms per cubic meter')
plt.ylabel('μg/m^3')
plt.xlabel('h')
plt.xticks(rotation=90)
plt.grid(True)
plt.legend()
plt.show()
#plt.show()

print(data.head())