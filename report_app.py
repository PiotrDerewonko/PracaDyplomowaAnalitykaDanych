import streamlit as st


st.set_page_config(layout="wide")
pages = {
        "Raporty": [
            st.Page("pages/02_reason.py", title="Ilość wypadków"),
            st.Page("pages/03_maps.py", title="Mapy"),

        ],

    }
pg = st.navigation(pages, position="sidebar")
pg.run()


