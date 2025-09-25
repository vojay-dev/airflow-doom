from airflow.sdk import dag, task
from pendulum import datetime


@dag(
    schedule="@daily",
    start_date=datetime(2025, 9, 1)
)
def very_important_dag():

    @task
    def transform_data():
        pass

    transform_data()

very_important_dag()
