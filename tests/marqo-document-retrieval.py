# open document
import marqo
import pprint


mq = marqo.Client(url='http://localhost:8882')

results = mq.index("my-first-index").get_document(document_id="article_591")

pprint.pprint(results)
