from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    "owner": "PauloToledo",
    "start_date": datetime(2025, 11, 6),
    "retries": 1
}

def say_hi():
    print("Hi from python operator")

with DAG(
    'roubo_de_carros_etl_dag',
    default_args=default_args,
    description='Pipeline ETL de Dados de Roubo de Carros por estado do Brasil',
    schedule_interval=None,  #executar manualmente
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="say_hi_task",
        python_callable=say_hi
    )
