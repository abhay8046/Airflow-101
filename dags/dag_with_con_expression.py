from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args={
    'owner':'Abhay',
    'retries':2,
    'retry_delay':timedelta(minutes=2)
}

def prints(cmd):
    print(cmd)


with DAG(
    default_args=default_args,
    dag_id='dag_with_con_expression',
    start_date=datetime(2024,9,3,10),
    #so usually we used to use @daily,@monthly previously but we can use cron to do that
    #schedule_interval='@daily'
    #while it can be difficult to promptly determine the interval, a website named crontab.guru can help you do that
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=prints,
        op_kwargs={'cmd':'Hello I am Abhay trying dag_with_con_expression'}
    )

task1