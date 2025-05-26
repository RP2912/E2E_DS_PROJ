# log_to_dagshub.py

import dagshub
import mlflow

# Initialize DagsHub repo for MLflow logging
dagshub.init(repo_owner='RP2912', repo_name='E2E_DS_PROJ', mlflow=True)

# Start MLflow run
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)
