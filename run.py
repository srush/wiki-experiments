import argparse
import argparse_config
import sys

def main():
    parser = argparse.ArgumentParser(
       description='Run translation experiments.')

    # parser.add_argument('--final_beam', type=int, 
    #                     help='size of the final beam')
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
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(open(data_out, 'w'))
    logger.addHandler(handler)
    
    formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
