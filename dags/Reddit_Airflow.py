from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
from Extract_Load.Reddit_Extract import connect_reddit
from Extract_Load.Reddit_Extract import transform_reddit
from  Extract_Load.Reddit_Extract import load_to_csv_data
    # Sales-Order Foodics
    
with DAG("Reddit_Airflow", start_date=datetime(2022, 12, 29),
schedule_interval='*/7 * * * *', max_active_runs=1, catchup=False) as dag:

    Reddit_script_A = PythonOperator(
        task_id="pull_data_from_reddit_api",
        python_callable=connect_reddit
    )

    Reddit_script_B = PythonOperator(
        task_id="Transform_Data",
        python_callable=transform_reddit
    )
    
    Reddit_script_C = PythonOperator(
        task_id="Load_Data_To_Csv",
        python_callable=load_to_csv_data
    )
    
    Reddit_script_A>> Reddit_script_B >> Reddit_script_C