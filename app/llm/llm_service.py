from app.config.settings import settings
from app.llm.nvidia_client import client
from app.utils.logger import logger

class LLMService:

    def ask(
        self,
        question: str,
        system_prompt: str,
        temperature: float = 0.2
    ) -> str:

        logger.info(f"Calling model: {settings.CHAT_MODEL}")
        response = client.chat.completions.create(
            model=settings.CHAT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=temperature
        )

        logger.info(f"Model response received")
        return response.choices[0].message.content


llm_service = LLMService()