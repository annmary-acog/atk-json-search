from atk_json_embeddings.pipeline import Pipeline
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceInstructEmbeddings
from atk_vectordbs.vector_dbs import FaissDB, MilvusDB
import typer
import os
os.environ['ATK_CONFIG_PATH'] = '../config'
from aganitha_base_utils import Config

app = typer.Typer()

config_json = Config().params('ingestion_config')

embeds_dict = {"OPENAI": OpenAIEmbeddings(),
               "HUGGINGFACE": HuggingFaceEmbeddings(model_name=config_json['MODEL_NAME']),
               "HUGGINGFACEINSTRUCT": HuggingFaceInstructEmbeddings(model_name=config_json['MODEL_NAME']),
               }

vectordb_dict = {"FAISS": FaissDB(), "MILVUS": MilvusDB()}


@app.command()
def run_pipeline(directory: str) -> None:
    """ Pipeline is called which pulls the data from all the resources we specify"""
    print(config_json)
    pipe = Pipeline(embed_model=embeds_dict[config_json['EMBED_MODEL']], vector_db=vectordb_dict[config_json['VECTOR_DB']])
    pipe.create_docs(directory=directory, content=config_json['CONTENT'], metadata_keys=config_json['METADATA_KEYS'])
    pipe.create_embeddings()


def main():
    app()


#run_pipeline(directory="/Users/annmary/fatty_liver_pubmed/pubmed_metadata/")
