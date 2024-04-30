import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import confusion_matrix


def accuracy(truth: list, pred: list) -> float:
    """
    This function calculates the model's accuracy given a list of truth labels and a parallel list of the model's predictions.
    :param truth: A list of truth labels
    :param pred: A parallel list to truth containing the model's predictions
    :return: The computed accuracy of the model
    """
    num_correct = 0
    for i in range(len(pred)):
        if pred[i] == truth[i]:
            num_correct = num_correct + 1
    return num_correct / len(pred)

# def plot_confusion_matrix(truth: list, pred: list, classes: list):
#     cm = confusion_matrix(truth, pred)
#     plt.figure(figsize=(8, 6))
#     sns.set(font_scale=1.2)
#     sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=classes, yticklabels=classes)
#     plt.xlabel('Predicted labels')
#     plt.ylabel('True labels')
#     plt.title('Confusion Matrix')
#     plt.show()
