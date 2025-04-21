# playwrightpp/llm/wrapper.py

from .prompts import build_prompt

class LLMWrapper:
    def __init__(self, provider):
        self.provider = provider

    def prompt(self, type_: str, **kwargs) -> str:
        prompt_text = build_prompt(type_, **kwargs)
        response = self.provider.complete(prompt_text)
        return response