
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
        self.attributes['care']['neg'] = 'megligent'
        self.attributes['care']['pos'] = 'meticulous'
        self.attributes['care']['score'] = kwargs.get('care', 0.0)
        self.attributes['cautious']['neg'] = 'reckless'
        self.attributes['cautious']['pos'] = 'cautious'
        self.attributes['cautious']['score'] = kwargs.get('cautious', 0.0)
        self.attributes['communication']['neg'] = 'reserved'
        self.attributes['communication']['pos'] = 'talkative'
        self.attributes['communication']['score'] = kwargs.get('communication', 0.0)
        self.attributes['compassionate']['neg'] = 'cruel'
        self.attributes['compassionate']['pos'] = 'kind'
        self.attributes['compassionate']['score'] = kwargs.get('compassionate', 0.0)
        self.attributes['empathy']['neg'] = 'unfeeling'
        self.attributes['empathy']['pos'] = 'empathetic'
        self.attributes['empathy']['score'] = kwargs.get('empathy', 0.0)
        self.attributes['extroversion']['neg'] = 'reclusive'
        self.attributes['extroversion']['pos'] = 'outgoing'
        self.attributes['extroversion']['score'] = kwargs.get('extroversion', 0.0)
        self.attributes['law_abiding']['neg'] = 'Unlawful'
        self.attributes['law_abiding']['pos'] = 'Lawful'
        self.attributes['law_abiding']['score'] = kwargs.get('law_abiding', 0.0)
        self.attributes['leadership']['neg'] = 'follower'
        self.attributes['leadership']['pos'] = 'leader'
        self.attributes['leadership']['score'] = kwargs.get('leadership', 0.0)
        self.attributes['magical']['neg'] = 'mundane'
        self.attributes['magical']['pos'] = 'enchanted'
        self.attributes['magical']['score'] = kwargs.get('magical', 0.0)
        self.attributes['opinionated']['neg'] = 'open minded'
        self.attributes['opinionated']['pos'] = 'dogmatic'
        self.attributes['opinionated']['score'] = kwargs.get('opinionated', 0.0)
        self.attributes['optimistic']['neg'] = 'pessimist'
        self.attributes['optimistic']['pos'] = 'optimist'
        self.attributes['optimistic']['score'] = kwargs.get('optimistic', 0.0)
        self.attributes['organized']['neg'] = 'irregular'
        self.attributes['organized']['pos'] = 'organized'
        self.attributes['organized']['score'] = kwargs.get('organized', 0.0)
        self.attributes['power']['neg'] = 'impotent'
        self.attributes['power']['pos'] = 'powerful'
        self.attributes['power']['score'] = kwargs.get('power', 0.0)
        self.attributes['rationality']['neg'] = 'irrational'
        self.attributes['rationality']['pos'] = 'reasonable'
        self.attributes['rationality']['score'] = kwargs.get('rationality', 0.0)
        self.attributes['resourcefulness']['neg'] = 'Unoriginal'
        self.attributes['resourcefulness']['pos'] = 'Ingenious'
        self.attributes['resourcefulness']['score'] = kwargs.get('resourcefulness', 0.0)
        self.attributes['self_control']['neg'] = 'indulgent'
        self.attributes['self_control']['pos'] = 'disciplined'
        self.attributes['self_control']['score'] = kwargs.get('self_control', 0.0)
        self.attributes['sociability']['neg'] = 'coy'
        self.attributes['sociability']['pos'] = 'gregarious'
        self.attributes['sociability']['score'] = kwargs.get('sociability', 0.0)
        self.attributes['spiritual']['neg'] = 'material'
        self.attributes['spiritual']['pos'] = 'spiritual'
        self.attributes['spiritual']['score'] = kwargs.get('spiritual', 0.0)
        self.attributes['temperament']['neg'] = 'nervous'
        self.attributes['temperament']['pos'] = 'relaxed'
        self.attributes['temperament']['score'] = kwargs.get('temperament', 0.0)
        self.attributes['visionary']['neg'] = 'pragmatic'
        self.attributes['visionary']['pos'] = 'idealist'
        self.attributes['visionary']['score'] = kwargs.get('visionary', 0.0)

        #self.attributes['']['neg'] = ''
        #self.attributes['']['pos'] = ''
        #self.attributes['']['score'] = kwargs.get('', 0.0)
    
        #self.ambition = kwargs.get('ambition', 0.0) # Idle <-> Ambitious
        #self.artsy = kwargs.get('artsy', 0.0) # Structural <-> Artistic
        #self.assurance = kwargs.get('assurance', 0.0) # Doubtful <-> Certain
        #self.care = kwargs.get('care', 0.0) # Negligent <-> Meticulous 
        #self.cautious = kwargs.get('cautious', 0.0) # Reckless <-> Cautious
        #self.communication = kwargs.get('communication', 0.0) # Reserved <-> Talkative
        #self.compassionate = kwargs.get('compassionate', 0.0) # Cruel <-> Kind
        #self.empathy = kwargs.get('empathy', 0.0) # Unfeeling <-> Empathetic
        #self.extroversion = kwargs.get('extroversion', 0.0) # Reclusive <-> Outgoing
        #self.law_abiding = kwargs.get('law_abiding', 0.0) # Unlawful <-> Lawful
        #self.leadership = kwargs.get('leadership', 0.0) # Follower <-> Leader
        #self.magical = kwargs.get('magical', 0.0) # Mundane <-> Enchanted
        #self.opinionated = kwargs.get('opinionated', 0.0) # Open Minded <-> Dogmatic
        #self.optimistic = kwargs.get('optimistic', 0.0) # Pessimist <-> Optimist
        #self.organized = kwargs.get('organized', 0.0) # Irregular <-> Organized
        #self.power = kwargs.get('power', 0.0) # Impotent <-> Powerful
        #self.rationality = kwargs.get('rationality', 0.0) # Irrational <-> Reasonable
        #self.resourcefulness = kwargs.get('resourcefulness', 0.0) # Unoriginal <-> Ingenious
        #self.self_control = kwargs.get('self_control', 0.0) # Indulgent <-> Disciplined
        #self.sociability = kwargs.get('sociability', 0.0) # Coy <-> Gregarious 
        #self.spiritual = kwargs.get('spiritual', 0.0) # Material <-> Spiritual
        #self.temperament = kwargs.get('temperament', 0.0) # Nervous <-> Relaxed
        #self.visionary = kwargs.get('visionary', 0.0) # Pragmatic <-> Idealist

        # Open Minded <=> Parochial
        # Intuitive <-> Logical
        # Self Serving <-> Altruistic

        # Other things to add:
        #   Fears
        #   Motivations
        #   How they act (Hard to quantify?) 
        #   Breaking point (What wouldn't this character normally do)
        #   Regrets
        #   Aspirations (Linked to motivation?)



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
        print(f"           Name: {self.name}")
        print(f"            Age: {self.age:.0f} years")
        print(f"         Weight: {self.weight:.0f} kg")
        print(f"     Profession: {self.profession}")
        for key, value in self.attributes.items():
            print(f"{key.title().replace('_',' '):>15s}: {value['neg'].title():>11s} [{self.slider_fill(value['score'], 7)}] {value['pos'].title():<11s} ({value['score']:4.1f})")
