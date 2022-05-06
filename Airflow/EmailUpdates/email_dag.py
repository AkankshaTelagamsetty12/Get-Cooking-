from airflow import DAG
from airflow import models
from airflow.operators import python_operator
import datetime
import pandas as pd

import os
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
import pandas as pd

def send_email():

    df= pd.read_csv('companydata.csv', index_col=0)

    user_df= pd.read_csv('df_user_register.csv')

    password= df.iloc[0,0]
    print("Dataframe------>")
    #print(user_df)
    user_emails=[]
    for i, row in user_df.iterrows():
        user_emails.append(str(row).split("\\t")[10])
        
    #user_emails= user_df.iloc[:,"2"]
    #print(user_emails)




    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("getcooking2022@gmail.com", password)
    server.sendmail("getcooking2022@gmail.com" ,
                    "akankshatelagamsetty@gmail.com" ,
                    "Hi! Is your kitchen stocked up and you don't know what to cook? We are here just for people like you. Subscribe to Get Cooking to receive reommendations of recipes from over 100k recipes online")
                    

    server.quit()



default_dag_args = {
    # The start_date describes when a DAG is valid / can be run. Set this to a
    # fixed point in time rather than dynamically, since it is evaluated every
    # time a DAG is parsed. See:
    # https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date
    'start_date': datetime.datetime(2022, 5, 5),
}



with models.DAG(
        'send_email_dag',
        schedule_interval='0 0 * * *',  #daily
        default_args=default_dag_args) as dag:
    def send_email():
    #print("Hello World")
        print("Inside send_email_dag")
        df= pd.read_csv('/home/airflow/gcs/dags/companydata.csv', index_col=0)

        user_df= pd.read_csv('/home/airflow/gcs/dags/df_user_register.csv')

        password= df.iloc[0,0]
        print("Dataframe------>")
        #print(user_df)
        user_emails=[]
        for i, row in user_df.iterrows():
            user_emails.append(str(row).split("\\t")[10])
            
        #user_emails= user_df.iloc[:,"2"]
        #print(user_emails)




        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("getcooking2022@gmail.com", password)
        server.sendmail("getcooking2022@gmail.com" ,
                        str(random.choice(user_emails)) ,
                        "Hi! Thank you for registering to Get Cooking! Is your kitchen stocked up and you don't know what to cook? We are here just for people like you. ")
                        

        server.quit()



    # An instance of an operator is called a task. In this case, the
    # hello_python task calls the "greeting" Python function.
    hellow_python = python_operator.PythonOperator(
        task_id='hellow',
        python_callable=send_email)

    
    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hellow_python 


