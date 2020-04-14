import numpy as np
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


# place any functions you need from CS1-3 here

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


# CS3
def normalize_minmax(data):
    size = data.shape

    col = size[1]

    for i in range(col):
        high = np.max(data[:, i])
        low = np.min(data[:, i])

        data[:, i] = (data[:, i] - low) / (high - low)
    return data


def knn_classifier_full(b, features, size, seed):
    # Step 2
    data = b.data[:, features]
    target = b.target

    # Step 3
    data = normalize_minmax(data)

    # Step 4
    data_train, data_part2, target_train, target_part2 = train_test_split(data, target, test_size=0.40,
                                                                          random_state=seed)
    # now data_part2 and target_part2 contains 40% of records
    # next, train_test_split() is called again
    # to split data_part2 and target_part2 into two sets of 20% each
    data_validation, data_test, target_validation, target_test = train_test_split(data_part2, target_part2,
                                                                                  test_size=0.50, random_state=seed)

    value = 0
    accuracy = 0
    best_target_predicted = 0
    # Step 5, 6, refer to: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    for k in range(1, 21):
        clf = neighbors.KNeighborsClassifier(k)  # instance of the classifier for a particular value of k
        clf.fit(data_train, target_train)  # Training data, Target shape
        target_predicted = clf.predict(data_validation)  # Predict the class labels
        result = get_metrics(target_validation, target_predicted, [1, 0])

        if result['accuracy'] > accuracy:
            accuracy = result['accuracy']
            value = k
            best_target_predicted = target_predicted

    # Step 7
    # Validation Set
    clf = neighbors.KNeighborsClassifier(value)  # instance of the classifier for the best value of k
    clf.fit(data_train, target_train)  # Training data, Target shape
    target_predicted = clf.predict(data_test)

    validation_set = get_metrics(target_validation, best_target_predicted, [1, 0])

    # Test Set
    test_set = get_metrics(target_test, target_predicted, [1, 0])

    out_results = {'best k': value,
                   'validation set': validation_set,
                   'test set': test_set}

    return out_results