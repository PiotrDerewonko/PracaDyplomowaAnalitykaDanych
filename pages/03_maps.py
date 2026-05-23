import streamlit as st
from pathlib import Path
import os
import pandas as pd


with st.container(width=1900, horizontal_alignment='left'):
    path_to_csv = os.path.join(os.getcwd(), Path(__file__).parent.parent, "data\\dane_przetworzone.csv")

    st.button('Załaduj dane')
    data = pd.read_csv(path_to_csv, low_memory=False)
    st.map(data.loc[data['brak_wspolrzednych'] == False])