from pathlib import Path

from app.embeddings.embedding_service import (
    embedding_service
)

from app.embeddings.vector_store import (
    vector_store
)

from app.ingestion.chunker import (
    chunk_text
)


DOCUMENTS_DIR = Path(
    "app/documents"
)


def ingest():

    for file in DOCUMENTS_DIR.glob(
        "*.txt"
    ):

        text = file.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(
            text=text
        )

        for index, chunk in enumerate(
            chunks
        ):

            embedding = (
                embedding_service.embed(
                    chunk
                )
            )

            vector_store.add_document(
                doc_id=f"{file.stem}_{index}",
                text=chunk,
                embedding=embedding
            )

            print(
                f"Stored: {file.stem}_{index}"
            )


if __name__ == "__main__":

    ingest()