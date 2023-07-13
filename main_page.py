import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def page4():
    st.markdown("# Page 4 🎉")
    st.sidebar.markdown("# Page 4 🎉")

def page5():
    st.markdown("# Page 5 🎉")
    st.sidebar.markdown("# Page 5 🎉")

def page6():
    st.markdown("# Page 6 🎉")
    st.sidebar.markdown("# Rage 6 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()