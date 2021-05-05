##Vaccine Tracker app


import streamlit as st
import datetime
import pandas as pd
import requests
import json

st.title('Vaccine Tracker')

st.components.v1.iframe("https://www.ris.world/wp-content/uploads/2020/12/COVID-19-Vaccine-Tracker-500x300-1.jpg",height=400)

choose=st.radio('Please choose a method', ['By States','By Pincode'])

if choose == 'By States':


    states_request = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
    states_codec=json.loads(states_request.text)
    states=pd.json_normalize(states_codec["states"])


    mapping_dict = pd.Series(states["state_id"].values,index = states["state_name"].values).to_dict()

    unique_state = list(states["state_name"].unique())
    unique_state.sort()


    state=st.selectbox('states',unique_state)



    districts_requests=requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(mapping_dict[state]))
    districts=json.loads(districts_requests.text)


    districts_codec=pd.json_normalize(districts["districts"])

    mapping_dict = pd.Series(districts_codec["district_id"].values,index = districts_codec["district_name"].values).to_dict()

    unique_districts = list(districts_codec["district_name"].unique())

    unique_state.sort()

    districts=st.selectbox('districts',unique_districts)


    date=st.date_input('Date input',datetime.datetime.today())
    date_input=date.strftime("%d-%m-%Y")


    district_id = mapping_dict[districts]
    try:
        URL=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, date_input))
        available=json.loads(URL.text)
        # available = cowin.get_availability_by_pincode(pin_code, date_input, min_age_limit)
        available_centers=pd.json_normalize(available["centers"],max_level=0)
        available_centers_org=available_centers.drop("sessions",axis=1)
        session=available_centers["sessions"]
        available_sessions=pd.DataFrame([i[0] for i in session])
        available_sessions_org=available_sessions.drop(["session_id","slots"],axis=1)
        final=pd.concat([available_centers_org,available_sessions_org],axis=1)
        st.table(final)
    except:
        st.info("Vaccine slot Not available for now,Try seatching another date")


if choose == 'By Pincode':
    # min_age_limit = 18
    try:
        pin_codec=pd.read_csv("pincode.csv")
        pin = list(pin_codec["Pincode"].unique())
        pin_code=st.selectbox('pincode',pin)
        date=st.date_input('Date input',datetime.datetime.today())
        date_input=date.strftime("%d-%m-%Y")
        # pin_code = "400080"
        # date_input = '03-05-2021'
        available_json = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin_code, date_input))
        available=json.loads(available_json.text)
        # available = cowin.get_availability_by_pincode(pin_code, date_input, min_age_limit)
        available_centers=pd.json_normalize(available["centers"],max_level=0)
        available_centers_org=available_centers.drop("sessions",axis=1)
        session=available_centers["sessions"]
        available_sessions=pd.DataFrame([i[0] for i in session])
        available_sessions_org=available_sessions.drop(["session_id","slots"],axis=1)
        final=pd.concat([available_centers_org,available_sessions_org],axis=1)
        st.table(final)
    except:
        st.info("Vaccine slot Not available, Try seatching another date")
