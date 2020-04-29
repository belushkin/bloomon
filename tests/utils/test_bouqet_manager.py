from bloomon.utils.stream import Stream
from bloomon.utils.bouqet_manager import BouqetManager


def test_read_stream(monkeypatch):
    monkeypatch.setattr('sys.stdin', open("data/input_stream.txt", "r", encoding="utf-8"))
    stream = Stream(BouqetManager())
    # print(stream.read_stream)
    for i in stream.readStream():
        print(i)
    assert True
