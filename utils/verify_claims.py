import os
import json
import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()


llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4o-mini",
    temperature=0
)


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def clean_llm_json(text: str) -> str:
    """
    Removes markdown code fences and extracts pure JSON
    """
    text = text.strip()

    
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    return text.strip()


def verify_claim(claim: str, claimed_value: str) -> dict:
    
    try:
        search = tavily.search(
            query=claim,
            max_results=5,
            include_raw_content=True
        )
        evidence = "\n".join(
            r.get("content", "") for r in search.get("results", []) if r.get("content")
        )
    except Exception as e:
        print("⚠️ Tavily search failed:", e)
        evidence = ""

    evidence = evidence.replace('"', "'")

    prompt = f"""
You are a professional fact-checker.

CLAIM:
{claim}

CLAIMED VALUE:
{claimed_value}

WEB EVIDENCE:
{evidence}

Rules:
- If evidence clearly confirms the value → Verified
- If evidence shows a newer or different value → Inaccurate
- If no reliable evidence → False

Return STRICT JSON ONLY:

{{
  "status": "Verified | Inaccurate | False",
  "correct_value": "string or null",
  "explanation": "one sentence",
  "source": "URL or source name"
}}
"""

    response = llm.invoke(prompt)
    raw_output = response.content

    try:
        cleaned = clean_llm_json(raw_output)
        result = json.loads(cleaned)

        return {
            "status": result["status"],
            "correct_value": result.get("correct_value"),
            "explanation": result["explanation"],
            "source": result["source"]
        }

    except Exception as e:
        print("⚠️ JSON parsing failed")
        print("RAW OUTPUT:\n", raw_output)

        return {
            "status": "False",
            "correct_value": None,
            "explanation": "Unable to verify due to malformed LLM response.",
            "source": "N/A"
        }
