# playwrightpp/llm/openai_provider.py

import os
from dotenv import load_dotenv
from openai import OpenAI
import time
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIProvider:
    def complete(self, prompt: str) -> str:
        with open(f"debug/{int(time.time())}_prompt.txt", "w") as f:
            f.write(prompt)

        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
