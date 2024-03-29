# basic query operation
import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

results = mq.index("my-first-index").get_stats()

pprint.pprint(results)
