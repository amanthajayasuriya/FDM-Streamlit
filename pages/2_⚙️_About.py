import streamlit as st

st.set_page_config(
    page_title="FakeCatcher",
    page_icon='🕸️'
)

st.title("About 🕵️‍♂️")
st.image('./about.jpg')

desc="""<p style="font-size:16px; "> The hope of this project is to use the data retrieved from Instagram about its fake accounts to 
build a model to predict whether an account is a fake or a real one before it makes a bigger 
impact on not only its users but also on the name ‘Instagram’.</p>"""

desc2="""<p style="font-size:16px;">Fakes and spammers are a major problem on all social media platforms, including Instagram.
The objective of this project is to find whether a certain Instagram account is a fake spammer or 
a genuine account, which will be helpful for the organization to keep the client avoided from the 
threats that can be faced due to the fake accounts’ engagements.
We are Developing Classification models to predict whether a certain account is fake or not and 
then the accuracy of the models can be compared to check which model will best suit the 
phenomena</p>"""
st.markdown(desc,unsafe_allow_html=True)
st.markdown(desc2,unsafe_allow_html=True)