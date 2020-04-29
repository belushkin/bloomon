import re
from bloomon.entities.flower import Flower
from bloomon.entities.bouqet_design import BouqetDesign


class BouqetManager(object):

    def __init__(self):
        self.bouqets = []
        self.flowers = []

    def manage(self, line):
        if not line:
            return None
        self.addFlower(line) if re.match('[a-z][L|S]', line) else self.addBouqet(line)

    def addBouqet(self, line):
        self.bouqets.append(BouqetDesign(line))

    def addFlower(self, line):
        self.flowers.append(Flower(line[0], line[1]))
