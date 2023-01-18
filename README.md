# Machine Learning

Includes all machine learning projects i've worked on, documenting my journey through machine learning.

<p align="center">
<img src="./img_agnes.PNG" width=400></img>
</p>

## Reference

**Models** <br>
[Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) <br>
[Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) <br>
[Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) <br>
[Support Vector Machine](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) <br>
[Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) <br>

**Tools** <br>
[Label Encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) <br>
[Train Test Split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) <br>
[Heat Map](https://seaborn.pydata.org/generated/seaborn.heatmap.html) <br>
[Confusion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) <br>
[Keras](https://www.tensorflow.org/api_docs/python/tf/keras) <br>
[Min Max Scaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) <br>

**Datasets** <br>
[QuickDraw](https://quickdraw.readthedocs.io/en/latest/) <br>

<!---
[]() <br>
--->

## Notes
Output, Input activation functions: Step function, Sigmoid, tanh. <br>
Hidden layer activation functions: ReLU, Leaky ReLU. <br>
For logistic regression use the 'binary cross entropy' loss function. <br>
Gradient descent agjust weights for each and every data sample per epoch. <br>
Stochastic Gradient descent adjusts weights for a random data sample per epoch. (Used for many samples) <br>
Minibatch Gradient descent adjust weights for a batch of random data samples per epoch. (Used for many samples) <br>
When using one hot encoding to categorize datasets use ```loss=categorical_cross_entropy```. <br>
Apply dropout layer after hidden layer.



