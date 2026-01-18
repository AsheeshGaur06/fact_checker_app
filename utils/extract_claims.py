import os
import json
import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4o-mini",
    temperature=0
)


PROMPT = PromptTemplate(
    input_variables=["text"],
    template="""
Extract ONLY factual claims involving:
- numbers
- dates
- statistics
- financial figures
- technical specifications

Return STRICT JSON ONLY as a list of objects with keys:
- claim
- claimed_value

Example:
[
  {{
    "claim": "India's GDP in 2023",
    "claimed_value": "$3.4 trillion"
  }}
]

TEXT:
{text}
"""
)


def clean_text(text: str) -> str:
    replacements = {
        "’": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "²": "^2"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def extract_claims(text: str):
    text = clean_text(text)  
    response = llm.invoke(PROMPT.format(text=text))

    content = response.content.strip()

  
    content = re.sub(r"^```json|```$", "", content, flags=re.MULTILINE).strip()

    try:
        claims = json.loads(content)
        
        claims = [
            {"claim": c.get("claim", ""), "claimed_value": c.get("claimed_value", "")}
            for c in claims
        ]
        return claims
    except json.JSONDecodeError:
        print("⚠️ JSON decode error from LLM response:")
        print(content)
        return []
