from airflow import DAG, task
from datetime import datetime,timedelta
from airflow.decorators import dag,task
from airflow.operators.python import PythonOperator

default_args={
    'owner':'Abhay',
    'retries':3,
    'retry_delay':timedelta(minutes=2)
}

@dag(
    dag_id='sum_dag_with_taskflow_api',
    default_args=default_args,
    start_date=datetime(2024,9,3,2)
)
def sum():
    @task(multiple_outputs=True)
    def get_num1(**kwargs):
        # return {
        #     'num1':20,
        #     'num2':30
        # }
        num1 = kwargs['dag_run'].conf.get('num1', 0)
        num2 = kwargs['dag_run'].conf.get('num2', 0)
        return{
            'num1':num1,'num2':num2
        }
    @task()
    def get_num2():
        return 10
    @task()
    def get_sum(num1, num2):
        sum=num1+num2
        print(f'sum of {num1} & {num2} is {sum}')

    num1=get_num1()
    num2=get_num2()
    sum=get_sum(num1=num1['num1'],num2=num1['num2'])


sum_dag_with_taskflow_api=sum()