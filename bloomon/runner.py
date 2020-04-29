from utils.stream import Stream

stream = Stream()
stream_gen = stream.read_stream()

for i in stream_gen:
    print(i)
