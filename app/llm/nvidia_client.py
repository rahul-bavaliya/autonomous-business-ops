import httpx
from openai import OpenAI

from app.config.settings import settings

client = OpenAI(
    api_key=settings.NVIDIA_API_KEY,
    base_url=settings.NVIDIA_API_URL,
    http_client=httpx.Client(
        verify=False,
        timeout=300.0
    )
)