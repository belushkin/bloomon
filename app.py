import sys


class Stream(object):

    def __init__(self):
        self.blank = False
        self.stream_gen = None

    def stream_reader(self):
        for line in sys.stdin:
            if not line:
                self.blank = True
            yield line

    def read_stream(self):
        self.stream_gen = (BouqetDesign(design) if self.blank else Flower(design) for design in self.stream_reader())


class BouqetManager(object):

    def __init__(self):
        self.bouqets = []
        self.flowers = []

    def add_bouqet(self):
        pass

    def add_flower(self):
        pass

class BouqetDesign(object):
    def __init__(self, design):
        self.design = design


class Flower(object):
    def __init__(self, design):
        self.design = design


stream = Stream()
stream.read_stream()

bucket_designs = []
flowers = []

