from airflow import DAG
from airflow import models
from airflow.operators import python_operator
import datetime
import pandas as pd
from Food_Search import *
import os
def food_search():
    #print("Hello World")
    ingred = ["flour", "eggs"]
    recipe = search_ingredients(ingred , 5)
    #print(recipe)
    recipe.to_csv (r'export_dataframe.csv', index = False, header=True)
    

    
'''
with models.DAG(dag_id="food_search_dag",
         start_date=datetime(2022,5,4),
         schedule_interval='*/15 * * * *',
         default_args=default_dag_args) as dag:

        task1 = PythonOperator(
        task_id="food_search",
        python_callable=food_search)
        '''
default_dag_args = {
    # The start_date describes when a DAG is valid / can be run. Set this to a
    # fixed point in time rather than dynamically, since it is evaluated every
    # time a DAG is parsed. See:
    # https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date
    'start_date': datetime.datetime(2022, 5, 4),
}



with models.DAG(
        'food_search_dag',
        schedule_interval='*/5 * * * *',  #daily
        default_args=default_dag_args) as dag:
    def food_search():
    #print("Hello World")
        ingred = ["flour", "eggs"]
        recipe = search_ingredients(ingred , 5)
        #print(recipe)
        print(os.getcwd())
        p= "/home/airflow/gcs/dags"
        print(os.listdir(p))
        print("Doneeeeeeeeeeeeeee------------------------------------")
        recipe.to_csv (r'/home/airflow/gcs/dags/input/export_dataframe.csv', index = False, header=True)
        #recipe.to_csv (r'https://storage.cloud.google.com/us-east1-airflowenv-ce25265b-bucket/dags/input/export_dataframe.csv', index = False, header=True)
        
        print("Saved---------")
        print(os.listdir("/home/airflow/gcs/dags/"))



    # An instance of an operator is called a task. In this case, the
    # hello_python task calls the "greeting" Python function.
    hello_python = python_operator.PythonOperator(
        task_id='hello',
        python_callable=food_search)

    
    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hello_python 


