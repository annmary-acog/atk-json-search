from atk_json_embeddings.pipeline import Pipeline
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from atk_vectordbs.vector_dbs import FaissDB, MilvusDB
import typer

app = typer.Typer()

embeds_dict = {"OPENAI": OpenAIEmbeddings(), "HUGGINGFACE": HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")}
vectordb_dict = {"FAISS": FaissDB(), "MILVUS": MilvusDB()}


@app.command()
def run_pipeline(directory: str, embeds="OPENAI", vector_db="FAISS") -> None:
    """ Pipeline is called which pulls the data from all the resources we specify"""
    pipe = Pipeline(embed_model=embeds_dict[embeds], vector_db=vectordb_dict[vector_db])
    pipe.create_docs(directory=directory, content="abstract", metadata_keys=("title", "url"))
    pipe.create_embeddings()


def main():
    app()

embeds = "OPENAI"
print(embeds_dict[embeds])