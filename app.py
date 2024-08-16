import streamlit as st
import landing
import WebClinic

PAGES = {
    "Home": landing,
    "Disease Prediction": WebClinic
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=0)
    page = PAGES[selection]
    page.run()

if __name__ == "__main__":
    main()