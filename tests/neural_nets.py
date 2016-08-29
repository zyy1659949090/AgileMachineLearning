from unittest import TestCase

from Models.neuralnets import wrapper_for_backprop_neural_network_cnn
from tests.data import DIGITS_DATASET
from tests.data import train, target
import numpy as np
from sklearn.cross_validation import train_test_split

class TestNeuralNetworks(TestCase):
    def test_something_that_matters(self):
        relative_test_set_size = 0.4

        # 20ish % is 'working'
        # 50ish % was where I thought I was stuck for a while
        # 95ish % is the highest I was getting
        #   Note that you want the test to pass consistently.  So whatever this
        # threshold is should be the worst-case-scenario training minimum
        accuracy_target = 0.5  # percent


        data = DIGITS_DATASET['data']
        targets = DIGITS_DATASET['target']

        train_x, test_x, train_y, test_y = train_test_split(
            train, target, test_size=relative_test_set_size)
#            data, targets, test_size=relative_test_set_size)
        score = wrapper_for_backprop_neural_network_cnn(train_x, train_y, test_x, test_y)
        self.assertGreaterEqual(score, accuracy_target)
        
        
