# Standard Problem Set

def most_endangered(species_list):
    lowestName = ""
    lowestpop = float('inf')

    for species in species_list:
        if species["population"] < lowestpop:
            lowestpop = species["population"]
            lowestName = species["name"]
        
    return lowestName

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))