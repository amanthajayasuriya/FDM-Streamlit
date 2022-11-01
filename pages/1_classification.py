from cProfile import label
from gettext import install
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import sklearn
import time

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("fake-account-classifier.sav","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"


#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval):
    
    prediction=classifier.predict([[Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval]])
    print(prediction)
    return prediction


  


def main():
  with st.sidebar:
    html_temp = """
    <div style="background-color:#bc2a8d;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Fake Account Athenticator ML App </h2>
    </div>
    <br><br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    Num_posts = st.number_input("Number Of Posts")
    Num_following = st.number_input("Number Of Following")
    Num_followers = st.number_input("Number Of Followers")
    Biography_length = st.number_input("Biography Length")
    Picture_availability = st.number_input("Picture Availability")
    Link_availability = st.number_input("Link Availability")
    Average_caption_length = st.number_input("Average Caption Length")
    Likes = st.number_input("Likes")
    Comments = st.number_input("Comments")
    Hashtag_count = st.number_input("Hashtag Count")
    Average_Post_interval = st.number_input("Average Post Interval")
    result=""
    if st.button("Predict"):

      with st.spinner(text='In progress'):
        time.sleep(0)
        result=predict_note_authentication(Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval)

        if result==0:
          st.success('Real')
        else:
          st.success('Fake')
    html_temp = """
    <br><br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)        
    #st.success('The output is {}'.format(result))
  with st.spinner(text='In progress'):
    time.sleep(2)
  result=predict_note_authentication(Num_posts,Num_following,Num_followers,Biography_length,Picture_availability,Link_availability,Average_caption_length,Likes,Comments,Hashtag_count,Average_Post_interval)
  st.subheader("Predicted result for account:")
  if result==0:
    
    st.success('Real')
  else:
    st.success('Fake')


#st.title("Instagram Fake Account Athenticator")        



if __name__=='__main__':
    main()

chart_data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=["Picture_availability", "result"])

st.bar_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Num_posts', 'Average_Post_interval', 'result'])

st.line_chart(chart_data)

