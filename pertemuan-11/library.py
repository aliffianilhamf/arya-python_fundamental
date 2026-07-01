import random 
import datetime as dt
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

print(random.choice([1,2,3,4,5]))
print(random.randint(a=0, b=100))

print(dt.date(2003, 4, 5))
umur = (dt.date(2003, 2, 5)) - (dt.date(2026, 7, 1))
print(umur/365)