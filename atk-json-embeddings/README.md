# atk-json-embeddings
This project uses the packages atk-embeddings and atk-vectordbs along with the class JsonConverter defined in this package to create a class Pipeline that extracts information from various json files, creates embeddings, indexes and stores them.

category: tech

The atk-json-embeddings contains the class Pipeline which utilises the class JsonConverter to extract data from json files in which the data is arranged in a particular schema. For each of these files, the Pipeline class calls the load_json function of the JSONConverter class which creates Document objects out of them by extracting the data which need to be the content and metadata parameters of the Document objects. These Document objects are combined and processed using the EmbeddingsPipeline class from the atk-embeddings package. The functions of this class are applied to the Documents, which creates chunks from the Documents, creates embeddings out of these chunks, indexes the embeddings and finally stores these vector embeddings. The EmbeddingsPipeline function takes as inputs the embedding model and the vectordb. The embedding model, model_name for the HuggingFace embeddings, vector db, content and keys are all input using a config file.
  
Created on Tue May  9 22:52:10 IST 2023
  Built with poetry

# Purpose
This project can be used to create a vector database of embeddings derived from the data contained in JSON files. This database can then be used as the knowledge base to retrieve information from.

# Installation
The libraries required for this package to work are listed in the pyproject.toml file under the tool.poetry.dependencies section. The package can be installed with the command `pip install atk-json-embeddings`

# How to use it
The command to run this package: `atk-json-embeddings` e.g. atk-json-embeddings "/path/to/directory/containing/files/"

The function to run this package: `run_pipeline(directory: str)`. e.g. run_pipeline("/path/to/directory/containing/files/")

The values for the embedding model, vector database, page content and metadata parameters of the Document object are given in the config file `ingestion_config.yaml`. 

Currently, the embedding models supported by this package are OpenAIEmbeddings, HuggingFaceEmbeddings and HuggingFaceInstructEmbeddings. The supported vector databases are FAISS and Milvus.



# Related information
https://python.langchain.com/en/latest/reference/modules/text_splitter.html

https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

https://python.langchain.com/en/latest/reference/modules/embeddings.html

https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

https://python.langchain.com/en/latest/reference/modules/embeddings.html
