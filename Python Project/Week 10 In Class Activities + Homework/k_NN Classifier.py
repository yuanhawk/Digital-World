from sklearn.model_selection import train_test_split
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np


# place any functions you need from CS1-3 here
# CS3
def normalize_minmax(data):
    size = data.shape

    col = size[1]

    for i in range(col):
        high = np.max(data[:, i])
        low = np.min(data[:, i])

        data[:, i] = (data[:, i] - low) / (high - low)
    return data


# CS1
def get_metrics(actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)

    output = {}

    output['confusion matrix'] = c_matrix
    output['total records'] = len(actual_targets)

    act = 0
    br = 0  # Bottom Row
    tr = 0  # Top Row
    for i in range(len(c_matrix)):
        act += c_matrix[i][i]
        br += c_matrix[-1][i]
        tr += c_matrix[0][i]

    output['accuracy'] = round(act / len(actual_targets), 3)
    output['sensitivity'] = round(c_matrix[-1][-1] / br, 3)  # correct,pos / total
    output['false positive rate'] = round(c_matrix[0][1] / tr, 3)  # false,pos / total neg

    return output


def knn_classifier(b, features, size, seed, k):
    # Step 2
    data = b.data[:, features]
    target = b.target

    # Step 3
    data = normalize_minmax(data)

    # Step 4
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=size, random_state=seed)

    # Step 5, 6, refer to: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    clf = neighbors.KNeighborsClassifier(k)
    clf.fit(data_train, target_train)  # Training data, Target shape
    target_predicted = clf.predict(data_test)  # Predict the class labels

    # Step 7
    results = get_metrics(target_test, target_predicted, [1, 0])

    return results