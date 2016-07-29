from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import numpy as np

def wrapper_for_nb_in_sklearn(data, current_state_to_predict):
    height, width = np.shape(data)
    smooshed = np.reshape(data,(height * width))
    le = LabelEncoder()
    le.fit(smooshed)
    encoded = le.transform(smooshed)
    clean = encoded.reshape(height,width)


    labels = np.array([x[-1] for x in clean])
    training = np.array([x[:-1] for x in clean])
    clf = MultinomialNB()
    clf.fit(training, labels)
    current_state_to_predict = np.array(current_state_to_predict)
    current_state_to_predict = current_state_to_predict.reshape(1,-1)
    thing = le.transform(np.array(current_state_to_predict))

    final =  clf.predict(thing)

    return le.inverse_transform(final)
    # return None
if __name__ == '__main__':
    PARTY_DATA_HEADER = ["Deadline", "Party", "Lazy", "Activity"]
    PARTY_DATA = [["Urgent", "Yes", "Yes", "Party"],
    	["Urgent", "No", "Yes", "Study"],
    	["Near", "Yes", "Yes", "Party"],
    	["None", "Yes", "No", "Party"],
    	["None", "No", "Yes", "Pub"],
    	["None", "Yes", "No", "Party"],
    	["Near", "No", "No", "Study"],
    	["Near", "No", "Yes", "TV"],
    	["Near", "Yes", "Yes", "Party"],
    	["Urgent", "No", "No", "Study"]]

    X = ["Near", "No", "Yes"]

    # Convert inputs to arrays to leverage numpy's reshaping and indexing
    data = np.array(PARTY_DATA)
    state_to_predict = np.array(X).reshape((1, -1))

    # Convert strs to ints for all Inputs:
    le = LabelEncoder()
    all_states = data.flatten()
    le.fit(all_states)

    intified_data = le.transform(data)
    intified_state_to_predict = le.transform(state_to_predict)

    # Pick out X and y from data:
    X = intified_data[:, :-1]
    y = data[:, -1]

    # Create and train model:
    clf = MultinomialNB(alpha=1., fit_prior=True,)
    clf.fit(X, y)

    # Predict for sample, and convert back to string:
    predicted_state_as_str = clf.predict(intified_state_to_predict)[0]

