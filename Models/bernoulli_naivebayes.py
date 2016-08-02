import unittest
#from Models.naivebayes import wrapper_for_nb_in_sklearn
from sklearn.naive_bayes import BernoulliNB


# Test data pulled from: https://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html
# Thanks, Marsland!

PARTY_DATA_HEADER = [
    "D-None", "D-Near", "D-Urgent", "Party", "Lazy", "Activity"
]

PARTY_DATA = [
    ["No", "No", "Yes", "Yes", "Yes", "Party"],
    ["No", "No", "Yes", "No", "Yes", "Study"],
    ["No", "Yes", "No", "Yes", "Yes", "Party"],
    ["Yes", "No", "No", "Yes", "No", "Party"],
    ["Yes", "No", "No", "No", "Yes", "Pub"],
    ["Yes", "No", "No", "Yes", "No", "Party"],
    ["No", "Yes", "No", "No", "No", "Study"],
    ["No", "Yes", "No", "No", "Yes", "TV"],
    ["No", "Yes", "No", "Yes", "Yes", "Party"],
    ["No", "No", "Yes", "No", "No", "Study"]
]

datakey = {
    "Yes":0,
    "No":1
}

labelkey = {
    "Party": 3,
    "Pub": 4,
    "Study": 5,
    "TV": 6
}

rlabelkey = {
    3: "Party",
    4: "Pub",
    5: "Study",
    6: "TV"
}


class TestNaiveBayes(unittest.TestCase):

    def test_party_solutions_with_pre_built_model(self):
        X = ["No", "Yes", "No", "No", "Yes"]
        predicted_class = wrapper_for_nb_in_sklearn(PARTY_DATA, X)
        self.assertEqual(predicted_class, "TV")


def wrapper_for_nb_in_sklearn(data, current_state_to_predict):
    """
        Import an already-built implementation, train it on the data,
    and return the class predicted given the current state.

        Note that the last column of data is assumed to be the variable
    to predict, and the order
    """
    # split features and labels
    factors = [x[0:5] for x in data]
    states = [x[5] for x in data]

    # convert data values into integers using datakey lookup
    features = []
    for i, row in enumerate(factors):
        features.append([])
        for j, value in enumerate(row):
            features[i].append(datakey[value])

    # convert labels into integers using labelkey
    labels = []
    for state in states:
        labels.append(labelkey[state])

    # convert predictions to integers using datakey
    predicts = []
    for i, pred in enumerate(current_state_to_predict):
        predicts.append(datakey[pred])

    # fit data and labels to model
    clf = BernoulliNB()
    clf.fit(features, labels)
    pred = clf.predict(predicts)

    # convert prediction back to string
    return rlabelkey[pred[0]]


if __name__ == "__main__":
    unittest.main()

