import nltk

from typing import List



from entity_extractor import EntityExtractor


class NLTKEntityExtractor(EntityExtractor):
    """
    Uses NLTK to extract named entities.
    """
    def __init__(self):
        self.parser = 'bla'

    # TODO: package has dependencies:
    # download: maxent_ne_chunker, averaged_perceptron_tagger, punkt, words
    # TODO: Instead of returning a list, return an object that adds metadata
    # on how entities were extracted. 
    def extract(self, text):
        tagged = nltk.pos_tag(nltk.word_tokenize(text))
        tree = nltk.ne_chunk(tagged)
        return [lf[0] for lf in tree.leaves() if lf[1]=='NN']