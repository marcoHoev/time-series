from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import itertools
import pickle
import logging

import warnings
warnings.filterwarnings('ignore')

formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger('ABCTEST')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)

temp = os.getcwd()
print(f'Current working directory: {temp}')
if '/project1' in temp:
    temp = temp.replace('/project1', '')
    os.chdir(temp)
    print(f'Switched to: {temp}')

data = pd.read_excel('data/QualidadeARO3.xlsx')
data = data.drop(columns='Ihavo')
rng = pd.date_range('1/1/2020 00:00', periods=8784, freq='1H')
data.index = rng

#adf_df = pd.DataFrame(index=data.columns, columns=['ADF_Statistic', 'p_value', 'Stationary'])
#sig_level = 0.05

#for i in range(0,data.shape[1]):
#    adf_tmp = adfuller(data.iloc[:,i])
#    adf_df.iloc[i,0] = adf_tmp[0]
#    adf_df.iloc[i,1] = adf_tmp[1]
#    adf_df.iloc[i,2] = True if adf_tmp[1] < sig_level else False

#print(adf_df.Stationary)

endog = data.Entrecampos
p_list = list(range(0,4))
q_list = list(range(0,4))
P_list = list(range(0,4))
Q_list = list(range(0,4))
model_dict = {}

tmp = os.getcwd()

for p,q,P,Q in itertools.product(p_list, q_list, P_list, Q_list):
    #print(f'{p},{q},{P},{Q}')
    file0 = os.path.join(tmp, f'models/proj1_1/{p}_{q}_{P}_{Q}.pkl')
    file1 = os.path.join(tmp, f'models/proj1/{p}_{q}_{P}_{Q}.pkl')
    if not os.path.isfile(file0) and not os.path.isfile(file1):
        try:
            model_fit = SARIMAX(endog, order=(p,0,q), seasonal_order=(P,0,Q, 24)).fit(disp=False) 
            model_dict[f'{p},{q},{P},{Q}'] = (model_fit.bic, model_fit.aic, model_fit.aicc)
            logger.info(f'{p},{q},{P},{Q}: {model_fit.bic},{model_fit.aic}, {model_fit.aicc}')
        except Exception as e:
            logger.info(f'Some error occured while fitting the model. \n {e}')
        try:
            with open(f'models/proj1_1/{p}_{q}_{P}_{Q}.pkl', 'ab') as f:
                pickle.dump(model_dict, f, pickle.HIGHEST_PROTOCOL)
        except:
            logger.info('Error while trying to save dict. Exiting')
            break
    else:
        logger.info(f'Already exists: {file0}')