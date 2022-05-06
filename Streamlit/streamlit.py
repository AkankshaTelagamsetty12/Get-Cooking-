from pydoc import cli
from random import sample
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import numpy as np
import pandas as pd
import streamlit_authenticator as stauth
from PIL import Image
import requests

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(credentials=credentials)
table_id = 'recipe-recommendation-348000.get_cooking.users'

# Perform query.
# Reference: https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#bigquery_simple_app_query-python
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

# Reference link: https://cloud.google.com/bigquery/docs/updating-data#python
def updateApihits(query):
    query_job = client.query(query)
    query_job.result()    
    assert query_job.num_dml_affected_rows is not None
    return query_job.num_dml_affected_rows

fullnames = run_query("SELECT fullname FROM " + table_id +  " LIMIT 10")
password_rows = run_query("SELECT password FROM " + table_id + " LIMIT 10")
password = []
names = []
unames = []
uname = run_query("SELECT username FROM " + table_id + " LIMIT 10")

# Print results.
for row in password_rows:
    password.append(row['password'])

for row in fullnames:
    names.append(row['fullname'])

for row in uname:
    unames.append(row['username'])

# Reference: https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031
hashed_passwords = stauth.Hasher(password).generate()

authenticator = stauth.Authenticate(names,unames,hashed_passwords,
    'stauth','mysecretkey',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    
    st.write("Success")
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    getCurrentUser = username
    apihits = run_query("SELECT apihits FROM " + table_id + " WHERE username = " + ("'%s'" % (getCurrentUser)))
    image = 'https://storage.cloud.google.com/get-cooking/image.jpeg'
    st.image(image, caption='', width=700)
    st.title('Get Cooking')
    st.write('An ML powered app!')

    title = st.text_input('Recipe Name', '', placeholder='Enter the keyword')
    st.write('The current recommendations is for ', title)
   
    
    if st.button('Submit'):
        api=[]
        api = run_query("SELECT apihits FROM " + table_id + " WHERE username = " + ("'%s'" % (getCurrentUser)))
        print(api)
        apicount = 0
        apihit = [d['apihits'] for d in api]
        
        apicount = apihit[0] + 1
        for x in api:
            for y in x:
                x.update({y: apicount})
        result = updateApihits("UPDATE " + table_id + " SET apihits = " + str(apicount) + " WHERE username = " + ("'%s'" % (getCurrentUser)))

        # res = requests.get(f"http://127.0.0.1:8000/{title}")
        # output = pd.read_csv(res)
        # print(output)
        # out = output.get("message")
        print(apicount)
        print(api)
        if apicount < 15:

            df = pd.read_csv('https://storage.googleapis.com/get-cooking/dataset/PP_users.csv')
            
            sample_data = df.head()
            st.dataframe(sample_data)
            st.write('The current recommendations is for ', title)
        else:
            st.write('User Request Limit Exceeded')
        #apihits = run_query("SELECT apihits FROM " + table_id + " WHERE username = " + ("'%s'" % (getCurrentUser)))

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')