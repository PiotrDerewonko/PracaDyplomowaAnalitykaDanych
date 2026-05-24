import pandas as pd
import streamlit as st
import os
from pathlib import Path

with st.container(width=1900, horizontal_alignment='left'):
    st.title('Typy samochodów biorących udział w wypadkach drogowych w Nowym Jorku')
    reason_of_accident = ['ACCELERATOR DEFECTIVE',
                          'AGGRESSIVE DRIVING/ROAD RAGE',
                          'ALCOHOL INVOLVEMENT',
                          'ANIMALS ACTION',
                          'BACKING UNSAFELY,'
                          'BRAKES DEFECTIVE',
                          'CELL PHONE (HAND-HELD)',
                          'CELL PHONE (HANDS-FREE)',
                          'DRIVER INATTENTION/DISTRACTION',
                          'DRIVER INEXPERIENCE',
                          'DRIVERLESS/RUNAWAY VEHICLE',
                          'DRUGS (ILLEGAL)',
                          'EATING OR DRINKING',
                          'EMPTY',
                          'FAILURE TO KEEP RIGHT',
                          'FAILURE TO YIELD RIGHT-OF-WAY',
                          'FATIGUED/DROWSY',
                          'FELL ASLEEP',
                          'FOLLOWING TOO CLOSELY',
                          'GLARE',
                          'HEADLIGHTS DEFECTIVE',
                          'ILLNESS',
                          'LANE MARKING IMPROPER/INADEQUATE',
                          'LISTENING/USING HEADPHONES',
                          'LOST CONSCIOUSNESS',
                          'OBSTRUCTION/DEBRIS',
                          'OTHER ELECTRONIC DEVICE',
                          'OTHER LIGHTING DEFECTS',
                          'OTHER VEHICULAR',
                          'OUTSIDE CAR DISTRACTION',
                          'OVERSIZED VEHICLE',
                          'PASSENGER DISTRACTION',
                          'PASSING OR LANE USAGE IMPROPER',
                          'PASSING TOO CLOSELY',
                          'PAVEMENT DEFECTIVE',
                          'PAVEMENT SLIPPERY',
                          'PEDESTRIAN/BICYCLIST/OTHER PEDESTRIAN ERROR/CONFUSION',
                          'PHYSICAL DISABILITY',
                          'PRESCRIPTION MEDICATION',
                          'REACTION TO UNINVOLVED VEHICLE',
                          'SHOULDERS DEFECTIVE/IMPROPER',
                          'STEERING FAILURE',
                          'TEXTING',
                          'TINTED WINDOWS',
                          'TIRE FAILURE/INADEQUATE',
                          'TOW HITCH DEFECTIVE',
                          'TRAFFIC CONTROL DEVICE IMPROPER/NON-WORKING',
                          'TRAFFIC CONTROL DISREGARDED',
                          'TURNING IMPROPERLY',
                          'UNSAFE LANE CHANGING',
                          'UNSAFE SPEED',
                          'UNSPECIFIED',
                          'USING ON BOARD NAVIGATION DEVICE',
                          'VEHICLE VANDALISM',
                          'VIEW OBSTRUCTED/LIMITED',
                          'WINDSHIELD INADEQUATE']
    choose_reason = st.multiselect('Wybierz typ samochodu', reason_of_accident, default=reason_of_accident)
    reload = st.button('Przelicz dane')
    tab_killed_injured, tab_reason_injured, tab_reason_killed = st.tabs(
        ['Zabici i Ranni', 'Najniebezpieczniejsze powody obrażeń',
         'Najniebezpieczniejsze powody śmierci'])
    if reload:
        path_to_csv = os.path.join(os.getcwd(), Path(__file__).parent.parent, "data\\dane_przetworzone.csv")
        data = pd.read_csv(path_to_csv, low_memory=False)
        data_to_analyze = pd.DataFrame()
        for i in range(1, 6):
            column = f'CONTRIBUTING FACTOR VEHICLE {i}'
            data_tmp = data[['BOROUGH', 'COLLISION_ID', column, 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED',
                             f'VEHICLE TYPE CODE {i}']]
            data_tmp = data_tmp.rename(columns={column: 'CONTRIBUTING FACTOR VEHICLE'})
            data_tmp = data_tmp.loc[data_tmp[f'VEHICLE TYPE CODE {i}'].notna()]
            data_to_analyze = pd.concat([data_to_analyze, data_tmp], ignore_index=True)
        data_to_analyze = data_to_analyze.loc[data_to_analyze['CONTRIBUTING FACTOR VEHICLE'].isin(choose_reason)]
        pivot_injured_killed = data_to_analyze.pivot_table(index='CONTRIBUTING FACTOR VEHICLE',
                                                           values=['NUMBER OF PERSONS INJURED',
                                                                   'NUMBER OF PERSONS KILLED',
                                                                   'COLLISION_ID'], aggfunc={
                'NUMBER OF PERSONS INJURED': 'sum',
                'NUMBER OF PERSONS KILLED': 'sum',
                'COLLISION_ID': 'count'
            })
        with tab_killed_injured:
            st.bar_chart(pivot_injured_killed.iloc[:, 1:].sort_values(by='NUMBER OF PERSONS INJURED', ascending=False), sort=False, height=650, stack=False)
            with st.expander(label='Dane Tabelaryczne'):
                st.dataframe(pivot_injured_killed.iloc[:, 1:])
        with tab_reason_injured:
            pivot_reason_injured = pivot_injured_killed.iloc[:, 1].div(pivot_injured_killed.iloc[:, 0],
                                                                       axis=0).sort_values(ascending=False) * 100
            st.bar_chart(pivot_reason_injured, height=650, sort=False)
            st.dataframe(pivot_reason_injured)
        with tab_reason_killed:
            pivot_reason_killed = pivot_injured_killed.iloc[:, 2].div(pivot_injured_killed.iloc[:, 0],
                                                                      axis=0).sort_values(ascending=False) * 100
            st.bar_chart(pivot_reason_killed, height=650, sort=False)
            st.dataframe(pivot_reason_killed)
