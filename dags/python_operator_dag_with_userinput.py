from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'abhay',
    'dag_retries': 2,
    'retry_delay': timedelta(minutes=2)
}

def get_sum(num1, num2, **kwargs):
    print(f"Received num1: {num1}, num2: {num2}")
    result = int(num1) + int(num2)
    print(f"Sum: {result}")

with DAG(
    default_args=default_args,
    dag_id='user_input_2sum',
    description='Get input nums from user to calculate sum',
    start_date=datetime(2024, 9, 3, 19),
    schedule_interval='@hourly',
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id='get_sum',
        python_callable=get_sum,
        op_kwargs={
            'num1': "{{ dag_run.conf.get('num1', 0) }}",
            'num2': "{{ dag_run.conf.get('num2', 0) }}"
        }
    )
task1