import re

from bloomon.entities.bouqet_design import BouqetDesign
from collections import defaultdict


class BouqetManager(object):
    """
        A class used to operate input data from the input stream.
        It takes input data and decide whether it is flower or design, then it stores it in internal storage
        for flowers or create bouqet design objects for further bouqets producing. It also stores designs in a list

        This class was designed under the pressure of time and can be optimized in different ways.
        First of all we have to decide do we consume all flowers and then produce bouqets or we produce bouqets
        on the fly.

        I don't see at the moment how we can optimize storage of the designs, we should walk over the list and check
        do we have enough flowers per every design. This is inefficient and can be optimized but I don't see clear
        solution at the moment. Probably we can store designs using TRIE datastructure or use another binary tree
        implementation

        Maintaining total amount of flowers both small and large can be improved either distinction between what
        kind of design do we have at the moment. Because current implementation produces huge if conditions and it
        looks ugly.

        Implementing reminder of the bouqet name must be improved as well. I think about maintaining priority queue
        with dictionary keys as flower specie and values as amount of left flowers large or small. Keeping it sorted
        will reduce amount of dict walking in order to fulfill left flowers in the bouqet.

        Attributes
        ----------
        _designs : list
            list of all designs we received from the input
        _flowersS : dict
            dictionary of small flower species together with amount we received from the input
        _flowersL : dict
            dictionary of large flower species together with amount we received from the input
        _totalFlowersS : int
            total amount of small flowers
        _totalFlowersL : int
            total amount of large flowers

        Methods
        -------
        manage()
            Consumes flower or design from the input and decide what to create flower or design
        addBouqetDesign()
            Creates object of bouqet design
        addFlower()
            Adds flower to the internal storage
        getDesigns()
            Returns existing designs
        getSmallFlowers()
            Returns dictionary with small flowers
        getLargeFlowers()
            Returns dictionary with large flowers
        produceBouqet()
            Check if we can create one of existing designs from the stream of incoming flowers.
            Most time consuming and core function of the assessment
        _getFlowers()
            Private helper function for cutting flowers from the input string
        _getTotalQuantityOfFlowers()
            Private helper function for cutting total quantity of flowers from the input string
    """

    EXCEPTION_MESSAGE = 'Booket design {} does not have quantity of flowers or it is less then 1'

    def __init__(self):
        self._designs = []

        self._flowersS = defaultdict(int)
        self._flowersL = defaultdict(int)

        self._totalFlowersS = 0
        self._totalFlowersL = 0

    def manage(self, line):
        """ void function consumes flower or design from the input and decide what to create flower or design

        :return: void
        """
        if not line:
            return None
        self.addFlower(line) if re.match('[a-z][L|S]', line) else self.addBouqetDesign(line)

    def addBouqetDesign(self, line):
        """ Creates new Bouqet design and store it in the list

        :return: void
        """
        quantity = self._getTotalQuantityOfFlowers(line)
        design = BouqetDesign(
            line[0],
            line[1],
            self._getFlowers(line[2:-int(len(str(quantity)))]),
            quantity
        )
        self._designs.append(design)

    def addFlower(self, line):
        """ Adds flower to the internal storage and increase total amount of flowers
            needed for checking if we can create bouqet or not

        :return: void
        """
        if line[1] == 'L':
            self._flowersL[line[0]] += 1
            self._totalFlowersL += 1
        else:
            self._flowersS[line[0]] += 1
            self._totalFlowersS += 1

    def getDesigns(self):
        """ Returns existing designs

        :return: list of existing designs
        :rtype: list
        """
        return self._designs

    def getSmallFlowers(self):
        """ Returns dictionary with small flowers

        :return: small flowers
        :rtype: dict
        """
        return self._flowersS

    def getLargeFlowers(self):
        """ void function consumes flower or design from the input and decide what to create flower or design

        :return: large flowers
        :rtype: dict
        """
        return self._flowersL

    def _getFlowers(self, row):
        """ Walk over the input string and cut flower specie and quantity then return it in dict

        :return: flowers species and quantities
        :rtype: dict
        """
        result = {}
        j = 0
        for i, val in enumerate(row):
            if not val.isdigit():
                result[val] = int(row[j:i])
                j = i + 1
        return result

    def _getTotalQuantityOfFlowers(self, row):
        """ Cut total amount of flowers from the tail of the string

        :raises: RuntimeError(EXCEPTION_MESSAGE)
            If quantity of flowers is 0 or does not exists at all
        :return: quantity of flowers
        :rtype: int
        """
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
        """ Produce bouqet from existing flowers, checks if it has enough flowers to do it.
            Walking over designs and checking can have bugs which has not been covered by tests, be careful
            If you find issue please cover it by tests

        :return: bouqet name
        :rtype: str
        """
        for design in self._designs:

            designFlowers = design.getFlowers()

            flowers = self._flowersL if design.getSize() == 'L' else self._flowersS
            total = self._totalFlowersL if design.getSize() == 'L' else self._totalFlowersS

            for key in designFlowers.keys():
                if sum(designFlowers.values()) > total:
                    break
                if key not in flowers:
                    break
                if flowers[key] < designFlowers[key]:
                    break
            else:
                # Building main bouqet name
                name = design.getName() + design.getSize()
                flowersName = defaultdict(int)
                for key in designFlowers.keys():
                    flowersName[key] += designFlowers[key]
                    if design.getSize() == 'L':
                        self._flowersL[key] -= designFlowers[key]
                        self._totalFlowersL -= designFlowers[key]
                    else:
                        self._flowersS[key] -= designFlowers[key]
                        self._totalFlowersS -= designFlowers[key]

                # Building bouqet reminder
                reminder = design.getFlowersQuantity() - sum(designFlowers.values())
                for key in designFlowers.keys():
                    if reminder <= 0:
                        break

                    if design.getSize() == 'L':

                        if reminder > 0 and self._flowersL[key] > 0:

                            if self._flowersL[key] >= reminder:
                                flowersName[key] += reminder
                                self._flowersL[key] -= reminder
                                self._totalFlowersL -= reminder
                                reminder = 0
                            else:
                                flowersName[key] += self._flowersL[key]
                                self._totalFlowersL -= self._flowersL[key]
                                reminder -= self._flowersL[key]
                                self._flowersL[key] = 0

                    else:

                        if reminder > 0 and self._flowersS[key] > 0:

                            if self._flowersS[key] >= reminder:
                                flowersName[key] += reminder
                                self._flowersS[key] -= reminder
                                self._totalFlowersS -= reminder
                                reminder = 0
                            else:
                                flowersName[key] += self._flowersS[key]
                                self._totalFlowersS -= self._flowersS[key]
                                reminder -= self._flowersS[key]
                                self._flowersS[key] = 0

                retName = ''.join('{}{}'.format(value, key) for key, value in flowersName.items())
                return design.getName() + design.getSize(), name + retName

        return None
