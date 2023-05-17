from langchain.document_loaders import JSONLoader
from langchain.docstore.document import Document
from typing import List, Tuple
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level='INFO')


class JsonConverter:
    def __init__(self, content: str, metadata_keys: Tuple) -> None:
        self.keys: Tuple = metadata_keys
        self.content = content
        self.metadata = self.json_meta_data()

    def json_meta_data(self):
        def meta_func(record: dict, metadata: dict):
            for key in self.keys:
                metadata[key] = record.get(key)
            return metadata
        return meta_func

    def load_json(self, file_path: str) -> List[Document]:
        logging.info("Creating Documents from JSON files")
        loader = JSONLoader(
            file_path=file_path,
            jq_schema='.',
            content_key=self.content,
            metadata_func=self.metadata
        )
        data = loader.load()
        return data
