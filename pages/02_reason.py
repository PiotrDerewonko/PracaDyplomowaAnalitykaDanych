import streamlit as st
import pandas as pd
from pathlib import Path
import os

with st.container(width=1900, horizontal_alignment='left', height=1200):
    st.title("Powody wypadków w dzielnicach Nowego Yorku")
    three_most_frequent_causes = st.checkbox(label='Pokaż 3 najczęstsze powody wypadków', value=False)
    show_borough = st.checkbox(label='Pokaż podział na dzielnice', value=False)
    reload = st.button(label='Przelicz dane')
    if reload:

        path_to_csv = os.path.join(os.getcwd(), Path(__file__).parent.parent, "data\\dane_przetworzone.csv")
        data = pd.read_csv(path_to_csv, low_memory=False)
        reason_of_accident = pd.DataFrame()
        data = data.loc[(data['brak_dzielnicy'] == False) ]
        data_to_analyze = pd.DataFrame()
        for i in range(1, 6):
            column = f'CONTRIBUTING FACTOR VEHICLE {i}'
            data_tmp = data[['BOROUGH', column, 'COLLISION_ID', f'VEHICLE TYPE CODE {i}']]
            data_tmp = data_tmp.rename(columns={column: 'CONTRIBUTING FACTOR VEHICLE'})
            data_tmp = data_tmp.loc[data_tmp[f'VEHICLE TYPE CODE {i}'].notna()]
            data_to_analyze = pd.concat([data_to_analyze, data_tmp], ignore_index=True)
        columns = None
        if show_borough:
            columns = ['BOROUGH']
        pivot_table = data_to_analyze.pivot_table(columns=columns, index='CONTRIBUTING FACTOR VEHICLE',
                                                  values='COLLISION_ID', aggfunc='count', margins=True, margins_name='Suma', fill_value=0)
        if not show_borough:
            pivot_table = pivot_table.rename(columns={'COLLISION_ID': 'Suma'})
        pivot_table = pivot_table.sort_values(by='Suma', ascending=False)
        pivot_table = pivot_table.drop(index='Suma')
        pivot_table_first_10 = pivot_table.iloc[0:10]
        pivot_table_other = pivot_table.iloc[10:]
        pivot_table_other = pivot_table_other.cumsum()
        pivot_table_other = pivot_table_other.iloc[-1].to_frame().T
        pivot_table_other = pivot_table_other.rename(index={pivot_table_other.index[0]: 'Other'})
        pivot_table_final = pd.concat([pivot_table_first_10, pivot_table_other], ignore_index=False)
        pivot_table_final = pivot_table_final.sort_values(by='Suma', ascending=False)
        tab_value, tab_to_100 = st.tabs(["Wykres wartości", "Wykres do 100 %"])
        with tab_value:
            if three_most_frequent_causes:
                pivot_table_final = pivot_table_final.iloc[0:3]
            if show_borough:
                pivot_table_final = pivot_table_final.iloc[:, :-1]
            st.bar_chart(pivot_table_final.T, height=650)
            with st.expander(label='Dane Tabelaryczne'):
                st.dataframe(pivot_table_final)
        with tab_to_100:
            pivot_sum = pivot_table_final.cumsum()
            pivot_sum = pivot_sum.iloc[-1]
            pivot_devided = pivot_table_final.div(pivot_sum, axis=1) *100
            st.bar_chart(pivot_devided.T, height=650)
            with st.expander(label='Dane Tabelaryczne'):
                st.dataframe(pivot_devided)


