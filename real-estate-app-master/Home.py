import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)
st.image("logo.jpg", caption="Created by Mandar Bhalerao", width=700)
# st.write("# Welcome to ")
# st.write("### Welcome to Gurgaon Real Estate Price Prediction and Analytics App")
# Center the welcome text using HTML
st.markdown(
    """
    <div style="text-align: center;">
        <h3>Welcome to Gurgaon Real Estate Price Prediction and Analytics App</h3>
    </div>
    """, unsafe_allow_html=True
)

st.write("##### 👉 Explore the available modules on the left to dive into detailed real estate analysis and predictions.")
st.write("##### 👉 Select a module to get started!")



st.sidebar.success("Select a demo above 👆")