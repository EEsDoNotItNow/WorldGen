
import numpy as np
import json

class settlement:

    def __init__(self, *args, **kwargs):
        self.type = None
        self.population = 0
        pass


    def card(self):
        """
            Print a card of this city
        """
        print(f"{self.type}")
        print(f"Population: {self.population:,d}")
        print(f"Land Area: {self.land_area:.1f} km^2 ({np.sqrt(self.land_area):.1f} km to the side)")
        print(f"Services: ")
        for service in self.services:
            # if self.services[service] < 1:
            #     continue
            print(f"   {service.title()}: {self.services[service]}")

        return self


    def generate(self, _type="town"):
        """
        _type: village, town, city, big-city
        """
        self.type = _type.title()

        # Roll population
        if "village" == self.type.lower():
            self.population = np.random.randint(20,1000,(3,))
            self.population = min(self.population)
        elif "town" == self.type.lower():
            self.population = np.random.randint(1000,8000,(5,))
            self.population = min(self.population)
        elif "city" == self.type.lower():
            self.population = np.random.randint(8000,12000)
        elif "big-city" == self.type.lower():
            self.population = np.random.randint(12000,100000)
        else:
            raise ValueError(f"Invalid settlement type {self.type}")

        # Land area in km^2
        self.land_area = self.population/np.random.randint(150,210)*2.58999

        # Load SV data
        with open("data/mideval.json","r") as fp:
            config_data = json.load(fp)

        # Munge SVs
        self.services = {}
        for profession in config_data['professions']:
            sv_adjust = 1+(sum(np.random.randint(1,5,(4,)))-10)/10
            config_data['professions'][profession]['sv'] *= sv_adjust

            self.services[profession] = self.population / config_data['professions'][profession]['sv']
            # print(self.services[profession])
            if self.services[profession] > 1:
                self.services[profession] = int(self.services[profession])
            else:
                if np.random.random() < self.services[profession]:
                    self.services[profession] = 1
                else:
                    self.services[profession] = 0




        return self
