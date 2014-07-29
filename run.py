import argparse
import argparse_config
import sys
import os

from dA import dA
import numpy
from theano.tensor.shared_randomstreams import RandomStreams
import theano
import theano.tensor as T
import logging

def main():
    parser = argparse.ArgumentParser(
       description='Run translation experiments.')

    parser.add_argument('--hidden_size', type=int, 
                        help='size of the hidden layer')
    # parser.add_argument('--iterations', type=int, 
    #                     help='iterations of subgrad')
    parser.add_argument('config', type=str)
    parser.add_argument('label', type=str)


    print >>sys.stderr, open(sys.argv[1]).read()
    argparse_config.read_config_file(parser, sys.argv[1])

    args = parser.parse_args()
    print args

    output_dir = os.path.join("Data", args.label)
    data_out = os.path.join(output_dir, "mydata.txt")
    print >>sys.stderr, data_out

    # Set up logging.
    logger = logging.getLogger("nn")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(open(data_out, 'w'))
    logger.addHandler(handler)
    
    formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    rng = numpy.random.RandomState(123)
    theano_rng = RandomStreams(rng.randint(2 ** 30))

    # Start code.
    x = T.matrix('x')
    da = dA(numpy_rng=rng, theano_rng=theano_rng, input=x,
            n_visible=28 * 28, n_hidden=args.hidden_size)

    logger.info("Starting")
    logger.info("ENDING")

if __name__ == "__main__":
    main()
    
