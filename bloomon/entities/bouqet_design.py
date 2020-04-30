
class BouqetDesign(object):
    """
        A class used to represent an Bouqet Design.
        It has all information about design from the input string passed here by bouqet manager

        Attributes
        ----------
        _name : str
            design name
        _size : int
            bouqet size: Large or Small flowers
        _flowers : dict
            amount of different flowers with it's quantity
        _flowersQuantity : int
            quantity of flowers in the bouqet

        Methods
        -------
        getName()
            Returns name of the bouqet design
        getSize()
            Returns size of the bouqet design
        getFlowers()
            Returns flowers of the bouqet design with it's must have amount
        getFlowersQuantity()
            Returns total quantity of the flowers in the design
    """

    def __init__(self, name, size, flowers, flowersQuantity):
        self._name = name
        self._size = size
        self._flowers = flowers
        self._flowersQuantity = flowersQuantity

    def getName(self):
        """ Returns name of the bouqet design

        :return: design name
        :rtype: str
        """
        return self._name

    def getSize(self):
        """ Returns size of the bouqet design

        :return: size of the bouqet, L | S
        :rtype: str
        """
        return self._size

    def getFlowers(self):
        """ flowers of the bouqet design with it's must have amount

        :return: flowers of the bouqet
        :rtype: dict
        """
        return self._flowers

    def getFlowersQuantity(self):
        """ Returns total quantity of the flowers in the design

        :return: quantity of flowers in the bouqet
        :rtype: int
        """
        return self._flowersQuantity
