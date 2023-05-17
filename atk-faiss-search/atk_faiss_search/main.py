from atk_faiss_search.search import get_embeds, fetch_results
import os
import typer

app = typer.Typer()

file_path = os.getenv("FAISS_PATH")


@app.command()
def search(query: str, results_count: int = 2):
    embeds_db = get_embeds(file_path)
    related_docs = fetch_results(query, embeds_db, results_count)
    for doc in related_docs:
        print("\n")
        print(doc)


def main():
    app()


# search("liver")
