
from . import char_base
import numpy as np

class spawner:

    def __init__(self, *args, **kwargs):
        # TODO: Load a demographics config
        self.demographics = kwargs.get('demographics')
        # TODO: Load a professions config
        # TODO: Load a names config
        pass


    def get_pop(self, number):
        """ Generate a population of a given size
        """
        pass


    def get_pop_iter(self, number):
        """ Generate a population of a given size and iterate through them
        """
        for i in range(number):
            if self.demographics is not None:
                profession = None
                roll = np.random.rand()
                # Find where we ended up
                for profession in self.demographics['professions']:
                    if roll > self.demographics['professions'][profession]['roll']:
                        break
            yield char_base(
                            name='Joe',
                            age=np.random.normal(30,10),
                            weight=np.random.normal(70,15),
                            profession=profession.title(),
                            temperament=np.random.normal(0,2),
                            law_abiding=np.random.normal(0,2),
                            opinionated=np.random.normal(0,2),
                           )

