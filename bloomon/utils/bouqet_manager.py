import re
from bloomon.entities.flower import Flower
from bloomon.entities.bouqet_design import BouqetDesign
from collections import defaultdict


class BouqetManager(object):

    EXCEPTION_MESSAGE = 'Booket design {} does not have quantity of flowers or it is less then 1'

    def __init__(self):
        self._designs = []
        self._flowersS = defaultdict(int)
        self._flowersL = defaultdict(int)

    def manage(self, line):
        if not line:
            return None
        self.addFlower(line) if re.match('[a-z][L|S]', line) else self.addBouqetDesign(line)

    def addBouqetDesign(self, line):
        quantity = self._getTotalQuantityOfFlowers(line)
        design = BouqetDesign(
            line[0],
            line[1],
            self._getFlowers(line[2:-int(len(str(quantity)))]),
            quantity
        )
        self._designs.append(design)

    def addFlower(self, line):
        if line[1] == 'L':
            self._flowersL[line[0]] += 1
        else:
            self._flowersS[line[0]] += 1

    def getDesigns(self):
        return self._designs

    def getSmallFlowers(self):
        return self._flowersS

    def getLargeFlowers(self):
        return self._flowersL

    def _getFlowers(self, row):
        result = {}
        j = 0
        for i, val in enumerate(row):
            if not val.isdigit():
                result[val] = int(row[j:i])
                j = i+1
        return result

    def _getTotalQuantityOfFlowers(self, row):
        quantity = 0

        if not row[-1].isdigit():
            raise RuntimeError(BouqetManager.EXCEPTION_MESSAGE.format(row))

        for index, _ in enumerate(row, 1):
            if not row[-index].isdigit():
                quantity = int(row[-index + 1:])
                break

        if quantity == 0:
            raise RuntimeError(BouqetManager.EXCEPTION_MESSAGE.format(row))

        return quantity

    def produceBouqet(self):
        for design in self._designs:
            designFlowers = design.getFlowers()

            flowers = self._flowersL if design.getSize() == 'L' else self._flowersS

            for key in designFlowers.keys():
                if key not in flowers:
                    break
                if flowers[key] < designFlowers[key]:
                    break
            else:

                name = design.getName() + design.getSize()
                for key in designFlowers.keys():
                    name += (str(designFlowers[key]) + key)
                    if design.getSize() == 'L':
                        self._flowersL[key] -= designFlowers[key]
                    else:
                        self._flowersS[key] -= designFlowers[key]

                return design.getName() + design.getSize(), name
        return None

