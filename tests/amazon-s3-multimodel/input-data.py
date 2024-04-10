import marqo
from marqo import Client
import pandas as pd

print(pd.__version__)

N = 100 # samples to use, the full dataset is ~220k
filename = "https://marqo-overall-demo-assets.s3.us-west-2.amazonaws.com/ecommerce_meta_data.csv"
data = pd.read_csv(filename, nrows=N)
data['_id'] = data['s3_http']
documents = data[['s3_http', '_id', 'price', 'blip_large_caption', 'aesthetic_score']].to_dict(orient='records')

#with open('my_array.pkl','wb') as f:
    #pickle.dump(documents, f, protocol=None, *, fix_imports=True, buffer_callback=None)


#import pickle 

#pickle.load(file, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=None)

client = Client(url='http://localhost:8882')
    
index_name = 'multimodal2'
settings = {
	"treatUrlsAndPointersAsImages": True,
	"model": "open_clip/ViT-L-14/laion2b_s32b_b82k",
	"normalizeEmbeddings": True,
}
    
response = client.create_index(index_name, settings_dict=settings)

device = 'cpu' # use 'cuda' if a GPU is available

res = client.index(index_name).add_documents(documents, client_batch_size=64, tensor_fields=["s3_http"], device=device)


