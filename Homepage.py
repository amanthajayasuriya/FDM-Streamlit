import streamlit as st


st.set_page_config(
    page_title="FakeCatcher",
    page_icon='🕸️'
)

st.title("The Bleak Reality of Cyber-Bullying in Sri Lanka")
st.sidebar.success("Select a page above.☝️")
st.image('./cyberbullying.jpg')

desc="""The lack of boundaries in the digital sphere has become a serious cause for concern. The consequences that come along with it are plenty. The youth in Sri Lanka make up the majority of active users on the web. Thus, they are also more likely to be at the receiving end of one of the most common virtual threats of the digital age – cyber-bullying."""
desc2="""According to the National Crime Prevention Council in the United States, cyber-bullying is “the process of using the internet, cell phones or other devices to send or post texts or images intended to hurt or embarrass another person.” It is similar to traditional forms of bullying, but with notable differences. Bullying, on a virtual platform, is targeted harassment intentionally carried out in an aggressive manner against a victim through an electronic source."""
st.markdown(desc,unsafe_allow_html=True)
st.markdown(desc2,unsafe_allow_html=True)

