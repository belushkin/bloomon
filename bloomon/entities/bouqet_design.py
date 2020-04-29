
class BouqetDesign(object):
    def __init__(self, name, size, flowers, flowersQuantity):
        self._name = name
        self._size = size
        self._flowers = flowers
        self._flowersQuantity = flowersQuantity

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def getFlowers(self):
        return self._flowers

    def getFlowersQuantity(self):
        return self._flowersQuantity
