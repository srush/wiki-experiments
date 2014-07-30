import logging
import json

#import numpy.random

import theano
import theano.tensor as T
import time
import numpy
# from collections import defaultdict

class StructuredMessage(object):
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))



def pre_train(layer, train_set_x,
              learning_rate=0.1, training_epochs=15, 
              batch_size=20, logger=None):

    index = T.lscalar()    
    x = layer.x
    cost, updates = layer.get_cost_updates(corruption_level=0.3,
                                           learning_rate=learning_rate)

    train_da = theano.function([index], cost, updates=updates,
         givens={x: train_set_x[index * batch_size:
                                  (index + 1) * batch_size]})
    n_train_batches = \
        train_set_x.get_value(borrow=True).shape[0] / batch_size
    start_time = time.clock()

    for epoch in xrange(training_epochs):
        c = []
        for batch_index in xrange(n_train_batches):
            c.append(train_da(batch_index))
        logger.info(StructuredMessage('PRETRAINING', 
                                      epoch=epoch, 
                                      mean=numpy.mean(c)))


    end_time = time.clock()
    training_time = (end_time - start_time)
