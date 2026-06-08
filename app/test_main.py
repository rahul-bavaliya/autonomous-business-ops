from openai import OpenAI
from app.config.settings import settings

client = OpenAI(
    base_url=settings.NVIDIA_API_URL,
    api_key=settings.NVIDIA_API_KEY
)

models = client.models.list()

for model in models.data:
    print(model.id)