import streamlit as st


st.set_page_config(layout="wide")
pages = {
        "Raporty": [
            st.Page("pages/02_reason.py", title="Ilość wypadków"),
            st.Page("pages/03_maps.py", title="Mapy"),
            st.Page("pages/04_type_of_cars.py", title="Typy samochodów w wypadkach"),
            st.Page("pages/05_kills_injured.py", title="Zabici i ranni"),

        ],

    }
pg = st.navigation(pages, position="sidebar")
pg.run()


