# let's print out the results:
import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

results = mq.index("my-first-index").search(
    q="What is the best outfit to wear on the moon?"
)

pprint.pprint(results)
