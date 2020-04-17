def simple_classification_model(list_samples):
    list_classes = []

    for sample in list_samples:
        petal_width = sample[-1]
        if petal_width < 0.7:
            list_classes.append('Iris-setosa')
        elif petal_width < 1.6:
            list_classes.append('Iris-versicolor')
        else:
            list_classes.append('Iris-virginica')

    return list_classes