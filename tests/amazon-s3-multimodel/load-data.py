import pandas as pd
import pickle

print(pd.__version__)

N = 100 # samples to use, the full dataset is ~220k
filename = "https://marqo-overall-demo-assets.s3.us-west-2.amazonaws.com/ecommerce_meta_data.csv"
data = pd.read_csv(filename, nrows=N)
data['_id'] = data['s3_http']
documents = data[['s3_http', '_id', 'price', 'blip_large_caption', 'aesthetic_score']].to_dict(orient='records')

#with open('my_array.pkl','wb') as f:
    #pickle.dump(documents, f, protocol=None, *, fix_imports=True, buffer_callback=None)
