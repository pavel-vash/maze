import utils

class Thing:
    def __init__(self, name):
        self.name = name
        self.strengthModifier = 0
        self.armorModifier    = 0
        self.healthModifier   = 0
        self.accuracy         = 0
        self.disposable       = False
        self.weight           = 0


    def modify_strenght(self, strenght):
        return strenght+self.strenghtModifier

    def modify_armor(self, armor):
        return armor+self.armorModifier

    def modify_health(self, health):
        return health+self.healthModifier

    def modify_accuracy(self, accuracy):
        return accuracy+self.accuracyModifier



    def read_from_file (self, fileStream):
        for line  in fileStream:
            words = utils.split_by_words(line)
            if not words:
                continue
            if  words[0] == "#Name":
                self.name = " ".join(words[1:])
            elif  words[0] == "#Health":
                self.healthModifier = int(words[1])
            elif words[0] == "#Strength":
                self.strengthModifier = int(words[1])
            elif words[0] == "#Armor":
                self.armorModifier = int(words[1])
            elif words[0] == "#Accuracy":
                self.accuracyModifier = int(words[1])
            elif words[0] == "#Weight":
                self.weight = int(words[1])
            elif words[0] == "#EndThing":
                return


