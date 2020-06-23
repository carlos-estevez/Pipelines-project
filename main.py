from argparse import ArgumentParser
from InternetUsers.csv import *

def parseArguments():
    parser=ArgumentParser()
    parser.add_argument("--internet",
                        dest="int", 
                        type=str,
                        nargs=2 
                        default="Try again",
                        help="Write two arguments"
    return parse_known_args()
     

args=parseArguments()
print(args)