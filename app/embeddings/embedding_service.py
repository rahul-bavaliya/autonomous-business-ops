from openai import OpenAI

from app.config.settings import settings
from app.utils.logger import logger
from app.llm.nvidia_client import client

class EmbeddingService:

    def __init__(self):

        self.client = client



    def embed(
        self,
        text: str
    ) -> list[float]:

        logger.info(
            "Creating embedding"
        )

        response = self.client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=text
        )

        return response.data[0].embedding


embedding_service = EmbeddingService()