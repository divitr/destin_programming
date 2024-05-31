import random
import matplotlib.pyplot as plt

from DataPoint import DataPoint
from KNN import KNN
from metrics import accuracy, plot_confusion_matrix

random.seed(42)


# You don't need to worry about the implementation of this function, just know that it generates your train and test data!
def generate_random_data(num_points: int, means: list, stds: list, train_test_ratio=4, num_classes=3):
    train = []
    test = []

    num_train_points = int((train_test_ratio / (train_test_ratio + 1)) * num_points)
    num_test_points = num_points - num_train_points

    for label in range(1, num_classes + 1):
        class_means = means[label - 1]
        class_stds = stds[label - 1]

        for _ in range(int(num_train_points / num_classes)):
            features = [random.gauss(class_means[i], class_stds[i]) for i in range(len(class_means))]
            data_point = DataPoint(features, label)
            train.append(data_point)

        for _ in range(int(num_test_points / num_classes)):
            features = [random.gauss(class_means[i], class_stds[i]) for i in range(len(class_means))]
            data_point = DataPoint(features, label)
            test.append(data_point)

    return train, test

# You don't need to worry about the implementation of this function, just know that it shows a plot of the data passed into it!
def visualize_data(data: list[DataPoint], num_classes: int):
    features = [data_point.feature_set for data_point in data]
    labels = [data_point.label for data_point in data]

    for label in range(num_classes):
        plt.scatter(
            [features[i][0] for i in range(len(features)) if labels[i] == label + 1],
            [features[i][1] for i in range(len(features)) if labels[i] == label + 1],
            label=f"Class {label + 1}"
        )

    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Data')
    plt.legend()
    plt.show()

# You can play around with these numbers if you like, but I *highly* recommend leaving them as they are until you finish the rest of the project!
num_points = 1000
means = [[.3, .6], [.6, .7], [.05, .001]]
stds = [[0.15, 0.15], [0.15, 0.05], [0.15, 0.15]]
num_classes = 3

# Generating our training and test data
training_data, test_data = generate_random_data(num_points, means, stds, num_classes = num_classes)
test_features = [data_point.feature_set for data_point in test_data]
test_labels = [data_point.label for data_point in test_data]

# Getting an idea of what our data looks like! It's always a good idea to understand your data before you begin designing and training a predictive model!
visualize_data(training_data, num_classes)

# Defining our K value and initializing a KNN model with the K value and our training data.
K = 100 #TODO: pick a K value!
knn_classifier = KNN(K, data = training_data)

# print(knn_classifier.predict(DataPoint([1.25, 1.2], None)))

# Evaluating our model!
predictions = [knn_classifier.predict(data_point) for data_point in test_data]
print(f"Accuracy: {accuracy(predictions, test_labels)}")
plot_confusion_matrix(test_labels, predictions, [1, 2, 3])
