"""

"""
import os
import sys
import logging

from typing import List, Dict
from nltk_entity_extractor import NLTKEntityExtractor

logger = logging.getLogger()

MIN_DREAM_TEXT_CHARS = 1


def main():
    source = sys.argv[1]

    input_is_not_filepath = not os.path.exists(source)
    input_is_invalid_dream = len(source) < MIN_DREAM_TEXT_CHARS
    if (source==None) or ((input_is_not_filepath) and (input_is_invalid_dream)):
        raise ValueError(
            f"Invalid source. Either input dream text greater" +
            "than {MIN_DREAM_TEXT_CHARS} characters or provide a valid file" +
            "path to read from.")

    if not input_is_not_filepath:
        with open(source, 'r') as fin:
            dream = fin.read()
        try:
            assert len(dream) > MIN_DREAM_TEXT_CHARS
        except AssertionError:
            raise AssertionError(f"Dream size must be > {MIN_DREAM_TEXT_CHARS}"+
                "for this parsing to make sense.")
    else:
        dream = source

    symbols = set(get_dream_symbols(dream))
    print(symbols)
    #associations = {symbol:get_associations(symbol) for symbol in symbols}
    #interpretation = get_interpretation(associations)
    #print_output(dream, associations, interpretation)


def get_dream_symbols(dream:str) -> List[str]:
    return NLTKEntityExtractor().extract(dream)    


def get_associations(symbol:str) -> List[str]:
    return ['asc_1', 'asc_2', 'asc_3']


def get_interpretation(associations:Dict[str, List[str]]) -> str:
    return "I think I should take up guitar"

def print_output(dream:str, symbols: List[str], 
    associations:Dict[str, List[str]], interpretation:str) -> None:
    print(dream)
    print(symbols)
    print(associations)
    print(interpretation)


if __name__ == "__main__":
    main()