import os
import sys

sys.path.append(os.getcwd())

from bloomon.utils.bouqet_manager import BouqetManager
from bloomon.utils.stream import Stream

manager = BouqetManager()
stream = Stream(manager)

for _ in stream.readStream():
    bouqet = manager.produceBouqet()
    if bouqet:
        print(bouqet[1])
