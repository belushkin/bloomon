import sys
from .bouqet_manager import BouqetManager


class Stream(object):

    def stream_reader(self):
        for line in sys.stdin:
            yield line

    def read_stream(self):
        return (BouqetManager(design) for design in self.stream_reader())
