# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import pickle
loaded_model = pickle.load(open('C:/models/weather_model.sav','rb'))

input_data=([[0,12.8,5,4.7]])

input_data_as_numpy_array=np.array(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
value=loaded_model.predict(input_data_reshaped)
print(value)

if(value[0]==0):
  print("drizzle")
elif(value[0]==1):
  print("fog")
elif(value[0]==2):
  print("rain")
elif(value[0]==3):
  print("snow")
elif(value[0]==4):
  print("sun")


