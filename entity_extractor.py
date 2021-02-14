from typing import List


class EntityExtractor():   
    def extract(self, text:str) -> List[str]:
        """
        Returns the entities in text using parser defined.
        """
        raise NotImplementedError