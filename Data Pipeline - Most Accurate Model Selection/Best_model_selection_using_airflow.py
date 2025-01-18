#This is a code to find the best accurate model, out of 3 models that will execute in form of tasks.

#Importing Libraries and operators for DAG

from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from random import randint
from airflow.operators.bash import BashOperator

#Creating a fucntion that would be called in tasks to get the random integer for model accuracy

def _training_model():
    return randint(1,10)

#Creating Function
"""Creating a function to return the value of the best model out of 3 tasks. For this we have to fetch/share the data 
between all the tasks"""

def _choose_best_model(ti):

    accuracies = ti.xcom_pull(task_ids=
                              ['training_model_A',
                               'training_model_B',
                               'training_model_C'
                               ])
    
    best_accuracy = max(accuracies)

    if(best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'

#Creating an instance of DAG Class

with DAG("my_dag",start_date=datetime(2025, 1, 1), schedule_interval="@daily", catchup=False) as dag:

    #Defining tasks

    training_model_A = PythonOperator(
        task_id="training_model_A",
        python_callable=_training_model
    )

    training_model_B = PythonOperator(
        task_id="training_model_B",
        python_callable=_training_model
    )

    training_model_C = PythonOperator(
        task_id="training_model_C",
        python_callable=_training_model
    )

    choose_best_model = BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=_choose_best_model
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate'"
    )

    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
    )

#Defining workflow dependencies by grouping the concurrent tasks together in a list

[training_model_A, training_model_B, training_model_C] >> choose_best_model >> [accurate, inaccurate]