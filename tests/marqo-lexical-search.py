# lexical search
import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

result = mq.index("my-first-index").search("marco polo", search_method="LEXICAL")

pprint.pprint(result)
