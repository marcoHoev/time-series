import pickle
import os

tmp = os.getcwd()
os.chdir('..')
file = os.path.join(tmp, 'models/proj1/0_0_0_0.pkl')

with open(file, 'rb') as f:
    data = pickle.load(f)
    print(data)
