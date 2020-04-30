from bloomon.utils.stream import Stream
from bloomon.utils.bouqet_manager import BouqetManager


def test_read_stream(monkeypatch):
    """
    Testing basic input stream
    """

    # given
    monkeypatch.setattr('sys.stdin', open("data/input_stream.txt", "r", encoding="utf-8"))
    manager = BouqetManager()
    stream = Stream(manager)

    # when
    for _ in stream.readStream():
        pass

    # then
    assert len(manager.getDesigns()) == 2
    assert len(manager.getLargeFlowers()) == 2
    assert len(manager.getSmallFlowers()) == 2


def test_producing_bouqets(monkeypatch):
    """
    Testing basic input stream and asserting bouqets
    """

    # given
    monkeypatch.setattr('sys.stdin', open("data/input_bouqets_stream.txt", "r", encoding="utf-8"))
    manager = BouqetManager()
    stream = Stream(manager)

    # when
    for _ in stream.readStream():
        bouqet = manager.produceBouqet()
        if bouqet and bouqet[0] == 'AS':
            assert bouqet[1] == 'AS3a4b6k'
            assert manager.getSmallFlowers() == {'a': 2, 't': 1, 'b': 10, 'k': 0}

    # then
    # assert False