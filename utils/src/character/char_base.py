
import numpy as np

class char_base:

    def __init__(self, *args, **kwards):

        self.name = kwards.get('name', 'N/A')
        self.age = kwards.get('age', np.random.normal(30,10))
        self.weight = kwards.get('weight', np.random.normal(70,15))
        # TODO: This generator stuff should be moved to a specific generation class, and 
        #   better defaults picked for these values.
        self.temperament = np.clip((0.5 + np.random.randn() * 0.2), 0, 1)
        self.law_abiding = np.clip((0.5 + np.random.randn() * 0.2), 0, 1)
        self.opinionated = np.clip((0.5 + np.random.randn() * 0.2), 0, 1)

        """ 
        Potential fields:
            ambitious
            artsy
            assurance
            cautious
            communication
            compassionate
            conscientiousness
            empath
            extroversion
            law_abiding
            leadership
            opinionated
            optimistic
            organized
            power
            rationality
            resourcefulness
            self-control
            sociability
            spiritual
            temperament
            visionary
        """


    def __str__(self):
        return f"char_base<{self.name}, {self.age}, {self.weight}>"


    def bar_fill(self, percent, _max=10, fill_char="#"):
        # Return a string to fill a progress bar
        chars = int(np.round(percent*_max))
        spaces = _max - chars
        return fill_char*chars + " "*spaces
        pass


    def card(self):
        # Print an info card
        print("")
        print(f"       Name: {self.name}")
        print(f"        Age: {self.age:.0f} years")
        print(f"     Weight: {self.weight:.0f} kg")
        print(f"Temperament: {self.temperament:4.0%} [{self.bar_fill(self.temperament, 20)}] ")
        print(f"Law Abiding: {self.law_abiding:4.0%} [{self.bar_fill(self.law_abiding, 20)}] ")
        print(f"Opinionated: {self.opinionated:4.0%} [{self.bar_fill(self.opinionated, 20)}] ")
