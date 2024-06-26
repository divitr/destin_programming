from DataPoint import DataPoint

class KNN:
    def __init__(self, k: int, data=None):
        if data is None:
            training_data = []
        else:
            self.training_data = data
        self.k = k

    def add_data_point(self, data_point: DataPoint):
        self.training_data.append(data_point)

    def add_data_points(self, data_points: list[DataPoint]):
        for data_point in data_points:
            self.add_data_point(data_point)

    def distance(self, feature_set_1: list, feature_set_2: list):
        """
        This function returns the Euclidean distance between feature_set_1 and feature_set_2.
        :param feature_set_1: A list of numerical values
        :param feature_set_2: A list of numerical values
        :return:
        """
        x1 = feature_set_1[0]
        x2 = feature_set_2[0]
        y1 = feature_set_1[1]
        y2 = feature_set_2[1]
        deltax = x1 - x2
        deltay = y1 - y2
        deltaxsquared = deltax**2
        deltaysquared = deltay**2
        distsquared = deltaxsquared + deltaysquared
        return distsquared**.5
    
    def distance_to_training_data_points(self, feature_set: list):
        """
        This function returns a parallel list to self.training_data containing the distance
         of the given feature set to every data point in self.training_data.
        :param feature_set: A list of numerical values representing the feature set
        :return: A list of the distances of each DataPoint
        """
        list = []
        for i in self.training_data:
            var = self.distance(i.feature_set, feature_set)
            list.append(var)
        return list
    
    def sorted_data_points(self, feature_set: list):
        """
        This function returns a list with the same elements as self.training_data, but sorted by their distance to the given feature_set.
        :param feature_set: A list of numerical values representing the feature set
        :return: A list of DataPoints, sorted by distance to feature_set
        """
        distances = self.distance_to_training_data_points(feature_set)
        zipped = list(zip(self.training_data, distances))
        zipped.sort(key=lambda x: x[1])
        zipped = [zipped[i][0] for i in range(len(zipped))]
        return zipped
    def majority_label(self, data_points_list: list[DataPoint]):
        """
        This function returns the majority label of the provided data points.
        :param data_points_list: A list of DataPoints whose majority label is to be determined
        :return: The majority label of data_points_list
        """
        
        label_frequency = {}
        for datapoint in data_points_list:
            if datapoint.label in label_frequency:
                label_frequency[datapoint.label] += 1
            else:
                label_frequency[datapoint.label] = 1
        return max(label_frequency, key=lambda key: label_frequency[key])
    def predict_helper(self, feature_set: list):
        """
        This function returns the predicted label for a given feature set.
        :param feature_set: A list of numerical values representing the feature set
        :return: The predicted label for the feature set
        """
        sorted_training_data = self.sorted_data_points(feature_set)
        first_k = sorted_training_data[:self.k]
        predicted_label = self.majority_label(first_k)
        return predicted_label

    def predict(self, data_point: DataPoint):
        return self.predict_helper(data_point.feature_set)
