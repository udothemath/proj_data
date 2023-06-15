# %%
from word_content import content_1, content_2, content
from langchain.llms.openai import OpenAI
from langchain.python import PythonREPL
from langchain.tools.python.tool import PythonREPLTool
from langchain.agents.agent_toolkits import create_python_agent
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.llms import OpenAI
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
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = OpenAI(openai_api_key=OPENAI_API_KEY, model_name="text-davinci-003")
# response = llm("explain large language model in one sentence")
# print(response)
# %%
current_prompt = f"幫我使用這份文件{content_2} 生成一段ppt大綱，有三個章節，每個章節只列出必要重點，每個重點提供說明，產出結果生成為原始markdown代碼"

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
messages = [
    SystemMessage(content="You are an expert ppt maker"),
    HumanMessage(
        content=current_prompt)
]
response = chat(messages)
print(response.content, end='\n')

# %%

template = """
You are an expert data scientist with an expertise in buidling deep learning models. Explain the concept of {concept} in a couple of lines
"""

prompt = PromptTemplate(
    input_variables=["concept"],
    template=template
)

# llm(prompt.format(concept="regularization"))

# %%
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain only specifying the input variable.
# print(chain.run("autoencoder"))
second_promtp = PromptTemplate(
    input_variables=["previous_response"],
    template="Repeat the first response then think about {previous_response}.Explain in traditional chineses"
)
chain_two = LLMChain(llm=llm, prompt=second_promtp)

overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)
explanation = overall_chain.run("cross valuation")
# %%

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)

texts = text_splitter.create_documents([explanation])

print(texts)
# %%
embeddings = OpenAIEmbeddings(model_name="ada")
# %%
query_result = embeddings.embed_query(texts[0].page_content)
print(query_result)
# %%
# %%


def run_pinecone():

    HAVE_INIT = False
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


def run_prompt_pinecone():
    pinecone.init(api_key=pinecone.api_key, environment=pinecone.env)
    index_name = "quickstart"
    search = Pinecone.from_documents(texts, embeddings, index_name=index_name)
    query = "What is the most difficult process on autoencoder?"
    result = search.similarity_search(query)


run_prompt_pinecone()
# %%
agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000),
    tool=PythonREPLTool(), verbose=True
)

agent_executor.run(
    "Find the roots if the quadratic functions 3 * x**2 * 2*x -1")

# %%
