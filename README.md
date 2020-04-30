```shell script
docker build -t bloomon .
docker run -it --rm bloomon
```

python -m pytest
cat data/input_stream.txt | python bloomon/runner.py


docker run --rm bloomon python -m pytest
docker run --rm bloomon cat data/input_stream.txt | python bloomon/runner.py