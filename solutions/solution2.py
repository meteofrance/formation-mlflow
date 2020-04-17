with mlflow.start_run(run_name='My_Model'):
    mlflow.log_param('MODEL_NAME', 'My Model')
    mlflow.log_metric('Accuracy', accuracy_score(Y, Y_pred))