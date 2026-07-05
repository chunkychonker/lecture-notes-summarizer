from dotenv import load_dotenv
load_dotenv()


import json
from anthropic import Anthropic

client = Anthropic()


SYSTEM_INSTRUCTION = """You are condensing lecture notes for exam review.
Preserve all definitions, formulas, dates, and named concepts.
Cut filler, examples, and repetition.

Return ONLY valid JSON (no markdown fences, no preamble) matching this schema:
{
  "concepts": ["..."],
  "definitions": [{"term": "...", "meaning": "..."}],
  "key_facts": ["..."],
  "exam_likely": ["..."],
  "review_questions": ["..."]
}

Detail level: "%s".
- "brief": only the most essential items, terse phrasing.
- "detailed": thorough coverage, fuller explanations.
"""

def summarize_text(text, detail):
    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 2000,
        system = SYSTEM_INSTRUCTION % detail,
        messages = [{"role": "user", "content": text}]
    )
    raw = response.content[0].text
    return json.loads(raw)



if __name__ == "__main__":
    sample = "Photosynthesis converts sunlight into energy. Chlorophyll absorbs light. It occurs in chloroplasts."
    print(summarize_text(sample, "brief"))
