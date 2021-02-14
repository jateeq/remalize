from typing import List

from entity_extractor import EntityExtractor


class NLTKEntityExtractor(EntityExtractor):
    """
    Uses NLTK to extract named entities.
    """
    def __init__(self):
        self.parser = 'bla'

    def extract(self, text):
        return ['sym_1', 'sym_2', 'sym_3']