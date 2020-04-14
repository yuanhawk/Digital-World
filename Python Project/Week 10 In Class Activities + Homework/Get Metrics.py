import numpy as np
from sklearn.metrics import confusion_matrix


def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)

    output = {}

    output['confusion matrix'] = c_matrix
    output['total records'] = len(actual_targets)


    act = 0
    for i in range(len(c_matrix)):
        act += c_matrix[i][i]
    output['accuracy'] = round(act / len(actual_targets), 3)

    sen = c_matrix[1][1] / (c_matrix[1][0] + c_matrix[1][1])
    output['sensitivity'] = round(sen, 3)

    fal = c_matrix[0][1] / (c_matrix[0][0] + c_matrix[0][1])
    output['false positive rate'] = round(fal, 3)

    return output

actual = ['cat', 'cat', 'cat', 'cat', 'bird', 'bird', 'bird', 'bird']
predicted = ['cat', 'cat', 'bird', 'bird', 'cat', 'bird', 'bird', 'bird']

# Negative, Positive, more interested in the Positive
labels = ['bird', 'cat']
cm = get_metrics(actual, predicted, labels)