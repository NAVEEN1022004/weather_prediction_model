
import streamlit as st
import numpy as np
import pickle


loaded_model = pickle.load(open('C:/models/weather_model.sav','rb'))

#function
def weather_prediction(preciptation,temp_max,temp_min,wind):
  inp=np.array([[preciptation,temp_max,temp_min,wind]]).astype(np.float64)
  pred=int(loaded_model.predict(inp))
  print(pred)

  return pred
  
 
 

    
def main():
    #title of web 
    st.title('weather_prediction_web')
    #getting inputdata
    precipitation=st.text_input('preciptation rate')
    temp_max=st.text_input('temp_max value')
    temp_min=st.text_input('temp_min value')
    wind=st.text_input('wind value')
    
    
    #code for prediction
    
    weather=""
    #creating a button
    if st.button("see the weather now"):
        weathe=int(weather_prediction(precipitation,temp_max,temp_min,wind))
        weather=int(weathe)
    print(weather)
    if(weather==0):
      weather='drizzle'
    elif(weather==1):
      weather='fog'
    elif(weather==2):
      weather='rain'
    elif(weather==3):
      weather='snow'
    elif(weather==4):
      weather='sun'
    st.success(weather)
if __name__=='__main__':
 main()
    