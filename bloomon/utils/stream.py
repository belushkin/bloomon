
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