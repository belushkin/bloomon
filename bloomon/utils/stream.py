import sys


class Stream(object):
    """
        A class used to consume standard input by generator and then yield it line by line to the bouqet manager

        Attributes
        ----------
        manager : BouqetManager
            Bouqet Manager instance

        Methods
        -------
        streamReader()
            Wrap and work with standard input
        readStream()
            Return stream generator
    """

    def __init__(self, manager):
        self.manager = manager

    def streamReader(self):
        """ Wrap and work with standard input

        """
        for line in sys.stdin:
            yield line

    def readStream(self):
        """ Returns generator of standard input

        :return: input generator
        :rtype: generator
        """
        return (self.manager.manage(design.strip()) for design in self.streamReader())
