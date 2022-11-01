import streamlit as st


st.set_page_config(
    page_title="FakeCatcher",
    page_icon='🕸️'
)

st.title("The Bleak Reality of Cyber-Bullying in Sri Lanka")
st.sidebar.success("Select a page above.☝️")
st.image('./cyberbullying.jpg')

desc="""The lack of boundaries in the digital sphere has become a serious cause for concern. The consequences that come along with it are plenty. The youth in Sri Lanka make up the majority of active users on the web. Thus, they are also more likely to be at the receiving end of one of the most common virtual threats of the digital age – cyber-bullying."""

st.markdown(desc,unsafe_allow_html=True)

