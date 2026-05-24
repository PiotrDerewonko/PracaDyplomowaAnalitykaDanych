import pandas as pd
import streamlit as st
import os
from pathlib import Path

from pandas import pivot_table

with st.container(width=1900, horizontal_alignment='left'):
    st.title('Typy samochodów biorących udział w wypadkach drogowych w Nowym Jorku')
    path_to_csv = os.path.join(os.getcwd(), Path(__file__).parent.parent, "data\\dane_przetworzone.csv")
    data = pd.read_csv(path_to_csv, low_memory=False)
    data_to_analyze = pd.DataFrame()
    for i in range(1, 6):
        column = f'VEHICLE TYPE CODE {i}'
        data_tmp = data[['BOROUGH', column, 'COLLISION_ID']]
        data_tmp = data_tmp.rename(columns={column: 'VEHICLE TYPE CODE'})
        data_tmp = data_tmp.loc[data_tmp[f'VEHICLE TYPE CODE'].notna()]
        data_to_analyze = pd.concat([data_to_analyze, data_tmp], ignore_index=True)
    pivot_table_type_of_cars = pivot_table(data_to_analyze, index='VEHICLE TYPE CODE', values='COLLISION_ID', aggfunc='count')
    pivot_table_type_of_cars = pivot_table_type_of_cars.sort_values(by='COLLISION_ID', ascending=False)
    st.bar_chart(pivot_table_type_of_cars, sort=False, height=650)
    pivot_table_type_of_cars = pivot_table_type_of_cars.rename(columns={'COLLISION_ID': 'Ilość samochodów w wypadkach'})
    with st.expander(label='Dane Tabelaryczne'):
        st.dataframe(pivot_table_type_of_cars)
