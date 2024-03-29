# open document
import marqo
import pprint

# delete documents:
mq.index("my-first-index").delete_documents(
    ids=["article_591", "article_602"]
)

# delete indexes
results = mq.index("my-first-index").delete()

pprint.pprint(results)
