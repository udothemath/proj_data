import pinecone
import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd

loadenv = load_dotenv(find_dotenv())
assert loadenv == True
pinecone.api_key = os.getenv('PINECONE_API_KEY')
pinecone.env = os.getenv('PINECONE_ENV')
print(pinecone.api_key)
print(pinecone.env)

HAVE_INIT = True

if HAVE_INIT is False:
    pinecone.init(api_key=pinecone.api_key, environment=pinecone.env)

# Giving our index a name
index_name = "quickstart"
# Delete the index, if an index of the same name already exists
if index_name in pinecone.list_indexes():
    pinecone.delete_index(index_name)

pinecone.create_index(index_name, dimension=3, metric="cosine")
print(pinecone.list_indexes())


df = pd.DataFrame(
    data={
        "id": ["A", "B"],
        "vector": [[1., 1., 1.], [1., 2., 3.]]
    })
print(df)
print("Done.")
