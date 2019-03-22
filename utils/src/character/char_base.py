
import numpy as np
from collections import defaultdict

class char_base:

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.weight = kwargs.get('weight')
        # TODO: This generator stuff should be moved to a specific generation class, and 
        #   better defaults picked for these values.
        self.profession = kwargs.get('profession')

        # Numeric Values
        # TODO: Move all these into a dictionary of relevent data
        self.attributes = defaultdict(lambda: {'score':0.0,'neg':'Undefined','pos':'Undefined'})
        
        #self.attributes['']['neg'] = ''
        #self.attributes['']['pos'] = ''
        #self.attributes['']['score'] = kwargs.get('', 0.0)
        self.attributes['ambition']['neg'] = 'idle'
        self.attributes['ambition']['pos'] = 'ambitious'
        self.attributes['ambition']['score'] = kwargs.get('ambition', 0.0)
        self.attributes['artsy']['neg'] = 'Structural'
        self.attributes['artsy']['pos'] = 'Artistic'
        self.attributes['artsy']['score'] = kwargs.get('artsy', 0.0)
        self.attributes['assurance']['neg'] = 'doubtful'
        self.attributes['assurance']['pos'] = 'certain'
        self.attributes['assurance']['score'] = kwargs.get('assurance', 0.0)
        self.attributes['cautious']['neg'] = 'reckless'
        self.attributes['cautious']['pos'] = 'cautious'
        self.attributes['cautious']['score'] = kwargs.get('cautious', 0.0)
        self.attributes['communication']['neg'] = 'reserved'
        self.attributes['communication']['pos'] = 'talkative'
        self.attributes['communication']['score'] = kwargs.get('communication', 0.0)
        self.attributes['compassionate']['neg'] = 'cruel'
        self.attributes['compassionate']['pos'] = 'kind'
        self.attributes['compassionate']['score'] = kwargs.get('compassionate', 0.0)
        self.attributes['law_abiding']['neg'] = 'Unlawful'
        self.attributes['law_abiding']['pos'] = 'Lawful'
        self.attributes['law_abiding']['score'] = kwargs.get('law_abiding', 0.0)
        self.attributes['spiritual']['neg'] = 'material'
        self.attributes['spiritual']['pos'] = 'spiritual'
        self.attributes['spiritual']['score'] = kwargs.get('spiritual', 0.0)
        self.attributes['temperament']['neg'] = 'nervous'
        self.attributes['temperament']['pos'] = 'relaxed'
        self.attributes['temperament']['score'] = kwargs.get('temperament', 0.0)
    
        #self.ambition = kwargs.get('ambition', 0.0) # Idle <-> Ambitious
        #self.artsy = kwargs.get('artsy', 0.0) # Structural <-> Artistic
        #self.assurance = kwargs.get('assurance', 0.0) # Doubtful <-> Certain
        #self.cautious = kwargs.get('cautious', 0.0) # Reckless <-> Cautious
        #self.communication = kwargs.get('communication', 0.0) # Reserved <-> Talkative
        #self.compassionate = kwargs.get('compassionate', 0.0) # Cruel <-> Kind
        self.conscientiousness = kwargs.get('conscientiousness', 0.0) # Negligent <-> Meticulous 
        self.empathy = kwargs.get('empathy', 0.0) # Unfeeling <-> Empathetic
        self.extroversion = kwargs.get('extroversion', 0.0) # Reclusive <-> Outgoing
        #self.law_abiding = kwargs.get('law_abiding', 0.0) # Unlawful <-> Lawful
        self.leadership = kwargs.get('leadership', 0.0) # Follower <-> Leader
        self.magical = kwargs.get('magical', 0.0) # Mundane <-> Enchanted
        self.opinionated = kwargs.get('opinionated', 0.0) # Open Minded <-> Dogmatic
        self.optimistic = kwargs.get('optimistic', 0.0) # Pessimist <-> Optimist
        self.organized = kwargs.get('organized', 0.0) # Irregular <-> Organized
        self.power = kwargs.get('power', 0.0) # Impotent <-> Powerful
        self.rationality = kwargs.get('rationality', 0.0) # Irrational <-> Reasonable
        self.resourcefulness = kwargs.get('resourcefulness', 0.0) # Unoriginal <-> Ingenious
        self.self_control = kwargs.get('self_control', 0.0) # Indulgent <-> Disciplined
        self.sociability = kwargs.get('sociability', 0.0) # Coy <-> Gregarious 
        #self.spiritual = kwargs.get('spiritual', 0.0) # Material <-> Spiritual
        #self.temperament = kwargs.get('temperament', 0.0) # Nervous <-> Relaxed
        self.visionary = kwargs.get('visionary', 0.0) # Pragmatic <-> Idealist


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
        print(f"         Name: {self.name}")
        print(f"          Age: {self.age:.0f} years")
        print(f"       Weight: {self.weight:.0f} kg")
        print(f"   Profession: {self.profession}")
        #print(f"Temperament: {'Nervous':>11s} [{self.slider_fill(self.temperament, 5)}] {'Relaxed':<11s} ({self.temperament:4.1f})")
        #print(f"Law Abiding: {'Unlawful':>11s} [{self.slider_fill(self.law_abiding, 5)}] {'Lawful':<11s} ({self.law_abiding:4.1f})")
        #print(f"Opinionated: {'Open Minded':>13s} [{self.slider_fill(self.opinionated, 5)}] {'Dogmatic':<11s} ({self.opinionated:4.1f})")
        for key, value in self.attributes.items():
            print(f"{key.title().replace('_',' '):>13s}: {value['neg'].title():>11s} [{self.slider_fill(value['score'], 5)}] {value['pos'].title():<11s} ({value['score']:4.1f})")

            #print(key, value)
