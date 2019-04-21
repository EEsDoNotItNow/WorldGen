
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
        return list(self.get_pop_iter(number))
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
                            age=np.random.normal(30, 10),
                            weight=np.random.normal(70, 15),
                            profession=profession.title(),  
                            ambition=np.random.normal(0, 1.5),
                            artsy=np.random.normal(0, 1.5),
                            assurance=np.random.normal(0, 1.5),
                            care=np.random.normal(0, 1.5),
                            cautious=np.random.normal(0, 1.5),
                            communication=np.random.normal(0, 1.5),
                            compassionate=np.random.normal(0, 1.5),
                            empathy=np.random.normal(0, 1.5),
                            extroversion=np.random.normal(0, 1.5),
                            law_abiding=np.random.normal(1, 1.5),
                            leadership=np.random.normal(-1, 1.5),
                            magical=np.random.normal(-1, 1.5),
                            opinionated=np.random.normal(0, 1.5),
                            optimistic=np.random.normal(0, 1.5),
                            organized=np.random.normal(0, 1.5),
                            power=np.random.normal(0, 1.5),
                            rationality=np.random.normal(0, 1.5),
                            resourcefulness=np.random.normal(0, 1.5),
                            self_control=np.random.normal(0, 1.5),
                            sociability=np.random.normal(0, 1.5),
                            spiritual=np.random.normal(0, 1.5),
                            temperament=np.random.normal(0, 1.5),
                            visionary=np.random.normal(0, 1.5),
                           )

