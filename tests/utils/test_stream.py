from bloomon.utils.stream import Stream


def test_read_stream(monkeypatch):
    monkeypatch.setattr('sys.stdin', open("data/input_stream.txt", "r", encoding="utf-8"))
    stream = Stream()
    # print(stream.read_stream)
    for i in stream.read_stream():
        print(i)
    assert True
