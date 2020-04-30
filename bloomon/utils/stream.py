import sys


class Stream(object):

    def __init__(self, manager):
        self.manager = manager

    def streamReader(self):
        for line in sys.stdin:
            yield line

    def readStream(self):
        return (self.manager.manage(design.strip()) for design in self.streamReader())
