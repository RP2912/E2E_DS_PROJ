<!-- End to end data science project -->
import dagshub
dagshub.init(repo_owner='RP2912', repo_name='E2E_DS_PROJ', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


  <!-- TOKEN="07191bf9e091891a2e6471ec77071ffddfaaa4fa"
  URL=" -->