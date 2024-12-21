import streamlit as st

st.title("EMC2/ Cloud Module")
st.header("App for testing AI APIs")
st.sidebar.image("https://seeklogo.com/images/E/ecole-hassania-des-travaux-publics-ehtp-logo-3D5770F217-seeklogo.com.png")
st.sidebar.header("Master Cloud Computing")
st.sidebar.selectbox('Select type of application', ['---choose application', 'Image Analysis', 'OCR', 'Thumbnail Image', 'Face Analysis'])
