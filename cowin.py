##Vaccine Tracker app

import streamlit as st
import datetime
from cowin_api import CoWinAPI
import pandas as pd

st.title('Vaccine Tracker')

cowin = CoWinAPI()

choose=st.radio('Please choose a method', ['By States','By Pincode'])

if choose == 'By States':

    states_codec = cowin.get_states()
    st.write(states_codec)
#     states=pd.json_normalize(states_codec["states"])
#     # states=pd.read_csv("states.csv")


#     mapping_dict = pd.Series(states["state_id"].values,index = states["state_name"].values).to_dict()

#     unique_state = list(states["state_name"].unique())
#     unique_state.sort()


#     state=st.selectbox('states',unique_state)


#     districts = cowin.get_districts(mapping_dict[state])

#     # districts

#     districts_codec=pd.json_normalize(districts["districts"])

#     mapping_dict = pd.Series(districts_codec["district_id"].values,index = districts_codec["district_name"].values).to_dict()

#     unique_districts = list(districts_codec["district_name"].unique())

#     unique_state.sort()

#     districts=st.selectbox('districts',unique_districts)


#     date=st.date_input('Date input',datetime.datetime.today())
#     date_input=date.strftime("%d-%m-%Y")


#     district_id = mapping_dict[districts]
#     date, min_age_limit='18'
#     available = cowin.get_availability_by_district(district_id, date_input, min_age_limit)
#     available_centers=pd.json_normalize(available["centers"])
#     st.write(available_centers)

# if choose == 'By Pincode':
#     min_age_limit = 18
#     pin_codec=pd.read_csv("pincode.csv")
#     pin = list(pin_codec["Pincode"].unique())
#     pin_code=st.selectbox('pincode',pin)
#     date=st.date_input('Date input',datetime.datetime.today())
#     date_input=date.strftime("%d-%m-%Y")


#     available = cowin.get_availability_by_pincode(pin_code, date_input, min_age_limit)
#     available_centers=pd.json_normalize(available["centers"])
#     st.write(available_centers)
# #
# # from cowin_api import CoWinAPI
# #
# # pin_code = "400080"
# # date = '03-05-2021'  # Optional. Default value is today's date
# # min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
# #
# # cowin = CoWinAPI()
# # available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
# # print(available_center)
# # print(available_centers)
