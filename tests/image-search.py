# image search with text
import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

results = mq.index("my-multimodal-index").search("animal")

pprint.pprint(results)


