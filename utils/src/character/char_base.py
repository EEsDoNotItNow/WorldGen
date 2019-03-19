
import numpy as np

class char_base:

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.weight = kwargs.get('weight')
        # TODO: This generator stuff should be moved to a specific generation class, and 
        #   better defaults picked for these values.
        self.profession = kwargs.get('profession')
        self.temperament = kwargs.get('temperament')
        self.law_abiding = kwargs.get('law_abiding')
        self.opinionated = kwargs.get('opinionated')
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


    def slider_fill(self, offset, size):
        # Produce a sliding scale of a given size characters.
        # assert size % 2 == 1, "Size must be odd"
        ret_val = ""
        max_arrows = int((size/2))+1
        offset = int(np.clip(np.round(offset), -max_arrows, max_arrows))
        if offset < 0:
            for i in range(max_arrows - abs(offset)):
                ret_val += " "
            for i in range(abs(offset)):
                ret_val += "<"
            while len(ret_val) < size:
                ret_val += " "
        elif offset == 0:
            for i in range(max_arrows-1):
                ret_val += " "
            ret_val += "|"
            while len(ret_val) < size:
                ret_val += " "

        else: # offset > 0
            for i in range(max_arrows-1):
                ret_val += " "
            for i in range(abs(offset)):
                ret_val += ">"
                if len(ret_val) >= size:
                    break
            while len(ret_val) < size:
                ret_val += " "

        return ret_val



    def card(self):
        # Print an info card
        print("")
        print(f"       Name: {self.name}")
        print(f"        Age: {self.age:.0f} years")
        print(f"     Weight: {self.weight:.0f} kg")
        print(f" Profession: {self.profession}")
        print(f"Temperament: {self.temperament:4.0%} [{self.bar_fill(self.temperament, 5)}] ")
        print(f"Law Abiding: {self.law_abiding:4.0%} [{self.bar_fill(self.law_abiding, 5)}] ")
        print(f"Opinionated: {self.opinionated:4.0%} [{self.bar_fill(self.opinionated, 5)}] ")
