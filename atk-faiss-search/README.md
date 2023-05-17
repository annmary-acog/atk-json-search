# atk-faiss-search

short_description: This project extracts the vector embeddings from a given pickle file containing FAISS indexes and returns the top n document chunks matching an input query.

category: tech

long_description: This project consists of 3 functions: 
The function `get_embeds` takes the file path of the pickle file which contains the vector embeddings of Documents created using FAISS. It opens this pickle file and returns the vector embeddings in it.
The function `fetch_results` takes in the query and the nuber of results that need to be displayed. This function uses the similarity_search_with_score method of FAISS to retrieve the Document chunks as well as the score of those results that best match the query given to the function. 
Finally, the function `search`, which is the main function, combines the two previously mentioned functions to form a comprehensive search function that takes in a query and the number of results that need to be displayed to output the search results derived from the vector embeddings.
  
Created on Thu May 11 14:52:49 IST 2023
  Built with poetry

# Purpose
This package was created to perform simple search and retrieve on a faiss database containing vector embeddings. This package can be used to retrieve info only from faiss indexed pickle files containing vector embeddings that were created using OpenAIEmbeddings, HuggingFaceEmbeddings or HuggingFaceInstructEmbeddings. 

# Installation
The libraries required for this package to work are listed in the pyproject.toml file under the tool.poetry.dependencies section. The package can be installed with the command `pip install atk-faiss-search`

# How to use it
The command to run this package: `atk-faiss-search`
e.g. atk-faiss-search "Obesity" --results-count 5

The function to run this package: `search(query: str, results_count: int)`. The default results_count is 4.
e.g. search("obesity", "5")

# Related information
https://python.langchain.com/en/latest/modules/indexes/vectorstores/examples/faiss.html
