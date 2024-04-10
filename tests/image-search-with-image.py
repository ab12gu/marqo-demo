# image search with image
import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

results = mq.index("my-multimodal-index").search(
    "https://docs.marqo.ai/2.0.0/Examples/marqo.jpg"
)

pprint.pprint(results)
