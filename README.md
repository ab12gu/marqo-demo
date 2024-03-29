# marqo-demo
Demo of marqo (multimodel vector search repository)




# Run simple query
$ docker rm -f marqo
$ docker run --name marqo -it -p 8882:8882 marqoai/marqo:latest
$ docker run --name marqo -it -p 8882:8882 -d marqoai/marqo:latest
$ python3 ./test/marqo-test.py
$ python3 ./test/marqo-results.py


# Alternate vector engines
$ https://github.com/currentslab/awesome-vector-search
