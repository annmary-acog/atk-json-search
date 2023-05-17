from atk_embeddings.pipeline import EmbeddingsPipeline
from langchain import embeddings
from atk_vectordbs.vector_dbs import BaseVectorDB
from atk_json_embeddings.json_loader import JsonConverter
from typing import Tuple
import os
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level='INFO')


class Pipeline:
    def __init__(self, embed_model: embeddings, vector_db: BaseVectorDB) -> None:
        self.docs = []
        self.pipe = EmbeddingsPipeline(embed_model=embed_model, vector_db=vector_db)

    def create_docs(self, directory: str, content: str, metadata_keys: Tuple) -> None:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            json = JsonConverter(content, metadata_keys)
            json_docs = json.load_json(file_path)
            self.docs.extend(json_docs)

    def create_embeddings(self) -> None:
        logging.info("Chunking Documents")
        chunks = self.pipe.chunk_docs(self.docs)
        logging.info("Creating embeddings")
        self.pipe.create_embeddings(chunks)
