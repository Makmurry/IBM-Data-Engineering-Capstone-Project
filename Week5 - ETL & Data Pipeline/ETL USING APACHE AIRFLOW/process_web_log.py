# import the libraries

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# defining DAG arguments

default_args = {
    'owner': 'Makmurry Akbar',
    'start_date': days_ago(1),
    'email': ['makmurry@ibm.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    }

# defining the DAG

dag = DAG(
    dag_id = 'process_web_log',
    default_args = default_args,
    description = 'DAG ETL Web Server Log',
    schedule_interval = timedelta(days=1),
    )

# Defining process 1 : extract_data 

extract_data = BashOperator(
    task_id = "extract_data",
    bash_command = 'cut -d" " -f1 $AIRFLOW_HOME/dags/capstone/accesslog.txt > $AIRFLOW_HOME/dags/capstone/extracted_data.txt',
    dag = dag,
    )

# Defining process 2 : transform_data 

transform_data = BashOperator(
    task_id = "transform_data",
    bash_command = 'grep -v "198.46.149.143" $AIRFLOW_HOME/dags/capstone/extracted_data.txt > $AIRFLOW_HOME/dags/capstone/transformed_data.txt',
    dag = dag,
    )

# Defining process 3 : load_data 

load_data = BashOperator(
    task_id = "load_data",
    bash_command = 'tar -cvf $AIRFLOW_HOME/dags/capstone/weblog.tar $AIRFLOW_HOME/dags/capstone/transformed_data.txt',
    dag = dag,
    )

# task Pipeline
extract_data >> transform_data >> load_data