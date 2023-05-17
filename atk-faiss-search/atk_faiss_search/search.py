import pickle
import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level='INFO')


def get_embeds(file_path: str):
    logging.info("Loading the embeddings")
    with open(file_path, "rb") as f:
        embeds_db = pickle.load(f)
    return embeds_db


def fetch_results(query, embeds_db, results_count):
    logging.info("Fetching the results")
    docs_and_scores = embeds_db.similarity_search_with_score(query=query, k=results_count)
    return docs_and_scores
