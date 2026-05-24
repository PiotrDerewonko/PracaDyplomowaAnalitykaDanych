import streamlit as st
from pathlib import Path
import os
import pandas as pd

with st.container(width=1900, horizontal_alignment='left'):
    st.title('Mapa wypadków drogowych w dzielnicach Nowego Yorku')
    path_to_csv = os.path.join(os.getcwd(), Path(__file__).parent.parent, "data\\dane_przetworzone.csv")

    borough_list = ['BRONX',
                    'BROOKLYN',
                    'MANHATTAN',
                    'QUEENS',
                    'STATEN ISLAND']
    borough = st.multiselect('Wybierz dzielnicę', borough_list, default=borough_list)
    count_of_accident = st.slider(min_value=0, max_value=533, value=[0, 533],
                                  label='Wybierz zakres ilośc wypadków w jednym miejscu')
    st.markdown(count_of_accident)

    reload = st.button('Załaduj dane')
    if reload:
        data = pd.read_csv(path_to_csv, low_memory=False)
        total_accidents = len(data)
        data = data.loc[data['BOROUGH'].isin(borough)]
        data = data.loc[(data['ile_wypadkow_w_danym_miejscu'] >= count_of_accident[0]) & (
                data['ile_wypadkow_w_danym_miejscu'] <= count_of_accident[1])]
        filtered_accidents = len(data)
        st.markdown(
            f'Znaleziono {filtered_accidents} z {total_accidents} wszystkich wypadków co stanowi {filtered_accidents / total_accidents * 100:.2f}% wszystkich wypadków')
        st.map(data.loc[data['brak_wspolrzednych'] == False],height=650)
        with st.expander(label='Dane Tabelaryczne'):
            st.dataframe(data)
