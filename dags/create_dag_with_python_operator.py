from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args={
    'owner':'Abhay',
    'retries':'2',
    'retry_delay':timedelta(minutes=2)
}

def sum(ti):
    num1=(ti.xcom_pull(task_ids='get_nums',key='num1'))
    num2=(ti.xcom_pull(task_ids='get_nums',key='num2'))
    text=ti.xcom_pull(task_ids='get_text')
    sum=num1+num2
    print(f'{text} {sum}')

def get_num(ti):
    ti.xcom_push(key='num1',value=23)
    ti.xcom_push(key='num2',value=78)

def get_text(ti):
    return 'The sum is'

with DAG(
    dag_id='python_operator_dag_v1',
    default_args=default_args,
    description='Our first python dag',
    schedule_interval='@daily',
    start_date=datetime(2024,9,3,3)

) as dag:
        task1=PythonOperator(
            task_id='first_task',
            python_callable=sum,
            op_kwargs={'num2':30}

        )
        task2=PythonOperator(
            task_id='get_nums',
            python_callable=get_num
        )
        task3=PythonOperator(
            task_id='get_text',
            python_callable=get_text
        )

[task2,task3]>>task1

