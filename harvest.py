############
# Part 1   #
############


class MelonType():

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller =is_bestseller
        self.name = name 
        self.pairings = []

    def add_pairing(self, pairing):

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    crenshaw = MelonType('cren', 1996, 'green', 'has seeds', 'not_bestseller', 'Crenshaw')
    yellow_watermelon = MelonType('yw', 2013, 'yellow', 'has seeds', 'bestseller', 'Yellow Watermelon')
    muskmelon = MelonType('musk', 1998, 'green',  'seedless', 'bestseller', 'Muskmelon')
    casaba = MelonType('cas', 2003, 'orange', 'has seeds', 'not bestseller', 'Casaba')
    crenshaw = MelonType('cren', 1996, 'green', 'has seeds', 'not_bestseller', 'Crenshaw')
    yellow_watermelon = MelonType('yw', 2013, 'yellow', 'has seeds', 'bestseller', 'Yellow Watermelon')
    

    all_melon_types.append(muskmelon.name)
    all_melon_types.append(casaba.name)
    all_melon_types.append(crenshaw.name)
    all_melon_types.append(yellow_watermelon.name)

    #for melons in the list:
        #read the melon.name of melon
        #append to list of names

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f'{melon.name} pairs with {melon.pairings}')

    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.name] = melon.code
    print(melon_dict)
melon_types = []



crenshaw = MelonType('cren', 1996, 'green', 'has seeds', 'not_bestseller', 'Crenshaw')
yellow_watermelon = MelonType('yw', 2013, 'yellow', 'has seeds', 'bestseller', 'Yellow Watermelon')
muskmelon = MelonType('musk', 1998, 'green',  'seedless', 'bestseller', 'Muskmelon')
casaba = MelonType('cas', 2003, 'orange', 'has seeds', 'not bestseller', 'Casaba')
melon_types.append(crenshaw)
melon_types.append(yellow_watermelon)
melon_types.append(muskmelon)
melon_types.append(casaba)


make_melon_type_lookup(melon_types)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods
    def __init__(self, shape, color, field, name_harvester):
        self.shape = shape
        self.color = color
        self.field = field
        self.name_harvester = name_harvester

    def is_sellable(self):
            if self.shape >= 5 and self.color >= 5:
                return True
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    for melon in melon_types:
        melon = melon.name

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 




#test gibberish
# muskmelon = MelonType('musk', 1998, 'green',  'seedless', 'bestseller', 'Muskmelon')
# casaba = MelonType('cas', 2003, 'orange', 'has seeds', 'not bestseller', 'Casaba')
# crenshaw = MelonType('cren', 1996, 'green', 'has seeds', 'not_bestseller', 'Crenshaw')
# yellow_watermelon = MelonType('yw', 2013, 'yellow', 'has seeds', 'bestseller', 'Yellow Watermelon')


# melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
# print(print_pairing_info(melon_types))

# make_melon_types()
# print_pairing_info(melon_types)