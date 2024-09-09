from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args={
    'owner':'Abhay',
    'retries':'3',
    'retry_delay':timedelta(minutes=2)
 

}


def prints(cmd):
    print(cmd)
with DAG(
    dag_id='catchup_dag_v2',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    start_date=datetime(2024,9,4)
) as dag:
    task1=PythonOperator(
        task_id='task1',
        python_callable=prints,
        op_kwargs={'cmd':"hello"}
        )