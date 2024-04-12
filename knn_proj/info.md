# Learning Goals
**This project achieves two goals:**
 - A gentle introduction to supervised learning techniques
 - An excercise in basic python
    - Abstraction
    - Functions
    - Data representation
    - Mathematical operations
 **By the end of this project, you should have a robust understanding of:**
   - Supervised learning
   - K-Nearest-Neighbors (KNN) algorithm
   - The implementation of the KNN algorithm
      - The intuition motivating supervised learning techniques, specifically KNN
      - Choosing an appropriate value for K
      - Evaluating performance of a machine learning model
# Project Overview
## Supervised Learning
 Before understanding what the KNN algorithm is or does, we should first learn about supervised learning. Supervised learning is a subset of machine learning in which the model is provided with features[^1] and a label[^2] for each data point. This allows the model to learn some relationship between the feature and label, such that when we provide it with a feature vector[^3] it hasn't seen before, it can predict an appropriate label.
## The KNN Algorithm
 Now that we have an understanding of what a supervised learning algorithm is, we can begin to explore the K-Nearest-Neighbors algorithm. The KNN algorithm is a simple yet powerful supervised learning algorithm used for classification and regression tasks. It is a non-parametric and lazy learning algorithm, meaning it doesn't make any assumptions about the underlying data distribution and doesn't require a training phase where it learns explicit model parameters[^4].
### The Intuition Behind KNN
 The intuition behind KNN is rather straightforward: given a new, unknown data point, the algorithm finds the K closest data points in the training set based on a distance metric[^5] and predicts the label of the new data point based on the majority label among its K nearest neighbors.
### Choosing a Value for K
 One of the key hyperparameters in the KNN algorithm is the value of K, which determines the number of neighbors to consider when making predictions. Choosing the right value of K is crucial, as it can significantly impact the performance of the algorithm.
### Evaluating the Performance of Our Algorithm
 To evaluate the performance of the KNN algorithm, various metrics can be used depending on the nature of the problem. For classification tasks, metrics such as accuracy, precision, recall, and F1-score are commonly used, while for regression tasks, metrics such as mean squared error (MSE) or R-squared are used. We'll get into this more once we have finished implementing the base algorithm and are choosing a value for K.
### More Resources
 KNN is very diferent from the type of programming you may be used to. If you find yourself unable to digest the material above, looking for visuals, or just wanting to learn more about the KNN algorithm, I recommend looking at some of these links (I've arranged them in order of digestibility):
  - [K-Nearest Neighbor - Medium](https://medium.com/swlh/k-nearest-neighbor-ca2593d7a3c4)
  - [K-Nearest Neighbor(KNN) Algorithm - GeeksForGeeks](https://www.geeksforgeeks.org/k-nearest-neighbours/#)
  - [What is the KNN algorithm? - IBM](https://www.ibm.com/topics/knn#:~:text=The%20k%2Dnearest%20neighbors%20(KNN)%20algorithm%20is%20a%20non,used%20in%20machine%20learning%20today.)
## Your Task
 Your task for this project consists of two parts:
  - Implementing the KNN algorithm
  - Evaluating performance of the algorithm, and using that to choose an optimal value for K.

 This is a complex and large project, so to help you out, I've provided some basic starter code. Note that this starter code contains a few different classes, something we covered briefly a few weeks ago. If you need a refresher on classes and Object-Oriented Programming I highly recommend checking out [this article](https://www.geeksforgeeks.org/python-classes-and-objects/) by GeeksForGeeks!

[^1]: Features are the information that the model is given; the inputs to the model.
[^2]: Labels are twhat we are asking the model to predict; the output of the model. An important clarification: A label as we usually think of it is categorical (e.g. cat or dog), but in the context of machine learning it may also be a continuous value (e.g. 1.234 or 0.987)!
[^3]: This is just a fancy way of saying when we give it an input!
[^4]: This information is not something I expect you to understand just yet, but is still something good to know.
[^5]: For our purposes, this metric will be the Euclidian (L2) norm, which you have alreadly learned as the Pythagorean Theorem.
