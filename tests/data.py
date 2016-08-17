

# Party test data pulled from: https://seat.massey.ac.nz/personal/s.r.marsland/MLBook.html
# Thanks, Marsland!

PARTY_DATA_HEADER = ["Deadline", "Party", "Lazy", "Activity"]
PARTY_DATA =       [["Urgent", "Yes", "Yes", "Party"],
                    ["Urgent", "No", "Yes", "Study"],
                    ["Near", "Yes", "Yes", "Party"],
                    ["None", "Yes", "No", "Party"],
                    ["None", "No", "Yes", "Pub"],
                    ["None", "Yes", "No", "Party"],
                    ["Near", "No", "No", "Study"],
                    ["Near", "No", "Yes", "TV"],
                    ["Near", "Yes", "Yes", "Party"],
                    ["Urgent", "No", "No", "Study"]]

# The above party data converted to binary-valued input variables:

BERNOULLI_PARTY_DATA_HEADER = [
    "D-None", "D-Near", "D-Urgent", "Party", "Lazy", "Activity"
]
BERNOULLI_PARTY_DATA = [
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


from sklearn.datasets import load_digits

DIGITS_DATASET = load_digits()
data = DIGITS_DATASET['data']
targets = DIGITS_DATASET['target']

#print (targets)
#print (data)

# https://www.kaggle.com/kobakhit/digit-recognizer/digit-recognizer-in-python-using-cnn/notebook
# https://www.kaggle.com/c/digit-recognizer/forums/t/2299/getting-started-python-sample-code-random-forest

import numpy as np
import pandas as pd
# create the training & test sets, skipping the header row with [1:]
dataset = pd.read_csv("Data/train.csv")
target = dataset[[0]].values.ravel()

train = dataset.iloc[:,1:].values


#test = dataset.iloc[]

# convert to array, specify data type, and reshape
target = target.astype(np.uint8)
#print target
train = np.array(train).reshape((-1, 28, 28)).astype(np.uint8)
#print train
