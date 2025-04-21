from .openai_provider import OpenAIProvider
from .wrapper import LLMWrapper

LLM = LLMWrapper(provider=OpenAIProvider())