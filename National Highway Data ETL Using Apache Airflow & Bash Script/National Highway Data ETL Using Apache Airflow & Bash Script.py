#!/usr/bin/env python
# coding: utf-8

# ![Screenshot%202025-01-12%20at%209.21.01%E2%80%AFAM.png](attachment:Screenshot%202025-01-12%20at%209.21.01%E2%80%AFAM.png)

# In[ ]:


# Import libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define default_args for the DAG
default_args = {
    'owner': 'dummy_name',
    'start_date': datetime.today(),
    'email': ['dummy_email@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval='@daily',
) as dag:

    # Task 1: Unzip data
    unzip_data = BashOperator(
        task_id='unzip_data',
        bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment',
    )

    # Task 2: Extract data from CSV
    extract_data_from_csv = BashOperator(
        task_id='extract_data_from_csv',
        bash_command=(
            "cut -d',' -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle-data.csv "
            "> /home/project/airflow/dags/finalassignment/csv_data.csv"
        ),
    )

    # Task 3: Extract data from TSV
    extract_data_from_tsv = BashOperator(
        task_id='extract_data_from_tsv',
        bash_command=(
            "cut -f2,5,6 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv "
            "| tr '\t' ',' > /home/project/airflow/dags/finalassignment/tsv_data.csv"
        ),
    )

    # Task 4: Extract data from fixed-width file
    extract_data_from_fixed_width = BashOperator(
        task_id='extract_data_from_fixed_width',
        bash_command=(
            "awk '{print substr($0, 1, 15) \",\" substr($0, 16, 20)}' "
            "/home/project/airflow/dags/finalassignment/payment-data.txt "
            "> /home/project/airflow/dags/finalassignment/fixed_width_data.csv"
        ),
    )

    # Task 5: Consolidate data
    consolidate_data = BashOperator(
        task_id='consolidate_data',
        bash_command=(
            "paste -d',' /home/project/airflow/dags/finalassignment/csv_data.csv "
            "/home/project/airflow/dags/finalassignment/tsv_data.csv "
            "/home/project/airflow/dags/finalassignment/fixed_width_data.csv "
            "> /home/project/airflow/dags/finalassignment/extracted_data.csv"
        ),
    )

    # Task 6: Transform data
    transform_data = BashOperator(
        task_id='transform_data',
        bash_command=(
            "awk -F',' '{OFS=\",\"; $4=toupper($4); print}' "
            "/home/project/airflow/dags/finalassignment/extracted_data.csv "
            "> /home/project/airflow/dags/finalassignment/transformed_data.csv"
        ),
    )

    # Define task dependencies
    unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data

