# open document
import marqo
import pprint

mq = marqo.Client(url='http://localhost:8882')

# delete documents:
mq.index("my-first-index").delete_documents(
    ids=["article_591", "article_602"]
)

# delete indexes
results = mq.index("my-first-index").delete()
results = mq.index("my-first-index").delete()

pprint.pprint(results)
