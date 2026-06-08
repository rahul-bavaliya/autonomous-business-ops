from dotenv import load_dotenv
import os

load_dotenv()



class Settings:

    NVIDIA_API_KEY= os.getenv(
        "NVIDIA_NIM_API_KEY"
    )

    NVIDIA_API_URL = os.getenv(
        "NVIDIA_NIM_API_URL"
    )

    CHAT_MODEL = os.getenv(
        "CHAT_MODEL"
    )

    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "nvidia/nv-embed-v1"
    )

settings = Settings()