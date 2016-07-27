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
	

	print wrapper_for_nb_in_sklearn(PARTY_DATA, X)