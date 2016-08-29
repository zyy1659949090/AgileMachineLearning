
#sklearn.neural_network import MLPClassifier
from sknn.mlp import Classifier, Convolution, Layer
from sklearn.metrics import accuracy_score



def wrapper_for_backprop_neural_network_code(train_x, train_y, test_x, test_y):
    score = None
    nn = Classifier(
            layers=[Layer('Sigmoid', units=5), 
            Layer('Softmax')], learning_rate=.001, n_iter=25)
    nn.fit(train_x, train_y)
    predicted = nn.predict(test_x)
    score = accuracy_score(predicted, test_y)
    return score

def wrapper_for_random_forest(test, train):
    # create and train the random forest
    # multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train, target)
    pred = rf.predict(test)

def wrapper_for_backprop_neural_network_cnn(train_x, train_y, test_x, test_y):
    score = None
    
 #   nn = Classifier(
 #       layers=[
 #       Convolution("Rectifier", channels=8, kernel_shape=(3,3)),
 #       Layer("Softmax")],
 #       learning_rate=0.02,
 #       n_iter=5)
 #   nn.fit(X_train, y_train)

    nn = Classifier(
            layers=[
            Convolution('Sigmoid', channels=8, kernel_shape=(3,3)),
            Layer('Softmax')], 
            learning_rate=.001,
            n_iter=10,
            dropout_rate=0.1)
    nn.fit(train_x, train_y)
 #   print(test_x.shape, train_x.shape)
    predicted = nn.predict(test_x)
    
    score = accuracy_score(predicted, test_y)
    return score