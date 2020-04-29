from utils.stream import Stream
from utils.bouqet_manager import BouqetManager

stream = Stream(BouqetManager())
stream_gen = stream.read_stream()

for i in stream_gen:
    print(i)
