FROM apache/airflow:2.9.0
USER airflow
RUN pip install pyspark bs4 selenium pandas
USER airflow
