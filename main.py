"""

"""
import logging
import argparse

from typing import List, Dict

logger = logging.getLogger()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--dream-file', help="dream text file")
    args = parser.parse_args()

    dream = None
    with open(args.dream_file, 'r') as fin:
        dream = fin.read()
    
    if (dream is None) | len(dream) < 1:
        logger.error("Invalid dream")
        print("Invalid dream file. Exiting")
        exit

    symbols = get_dream_symbols(dream)
    associations = {symbol:get_associations(symbol) for symbol in symbols}
    interpretation = get_interpretation(associations)

    print_output(dream, associations, interpretation)


def get_dream_symbols(dream:str) -> List[str]:
    return ['sym_1', 'sym_2', 'sym_3']


def get_associations(symbol:str) -> List[str]:
    return ['asc_1', 'asc_2', 'asc_3']


def get_interpretation(associations:Dict[str, List[str]]) -> str:
    return "I think I should take up guitar"

def print_output(dream:str, associations:Dict[str, List[str]], 
    interpretation:str) -> None:
    print(dream)
    print(associations)
    print(interpretation)


if __name__ == "__main__":
    main()