mlflow.set_experiment('Comparaison')

with mlflow.start_run(run_name='My_Model'):

    params = {}
    params['MODEL_NAME'] = 'My_Model'
    params['TRAIN_SIZE'] = len(X_train)
    params['TEST_SIZE'] = len(X_val)
    mlflow.log_params(params)

    predictions = simple_classification_model(X_val)

    metrics = {}
    metrics['Accuracy'] = accuracy_score(Y_val, predictions)
    metrics['Precision'] = precision_score(Y_val, predictions, average='macro')
    metrics['Recall'] = recall_score(Y_val, predictions, average='macro')
    metrics['Training Time'] = 0
    mlflow.log_metrics(metrics)

    cm = confusion_matrix(Y_val, predictions)
    plot_confusion_matrix(cm, ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
                            'Confusion matrix '+name)
    mlflow.log_artifact('matrix.png')