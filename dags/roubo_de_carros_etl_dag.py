from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from src.spark_session import get_spark
from src.pipeline import run_pipeline
from src.utils.paths import DATA_DIR, RAW_DIR, CURATED_DIR, STAGING_DIR
RAW_PATH = RAW_DIR / "roubo_raw.csv"
STAGING_PATH = STAGING_DIR / "roubo.parquet"

def run_etl():
    spark = get_spark("roubo_de_carros_etl")
    run_pipeline(spark, RAW_PATH, STAGING_PATH)

with DAG(
    dag_id="roubo_de_carros_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    etl_task = PythonOperator(
        task_id="etl_task",
        python_callable=run_etl,
    )
