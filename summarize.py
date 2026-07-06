from dotenv import load_dotenv
load_dotenv()

import os
from pypdf import PdfReader

import json
from anthropic import Anthropic

client = Anthropic()


def read_file_text(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


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



def to_markdown(data, source_name):
    lines = [f"# Study Sheet: {source_name}\n"]

    if data.get("concepts"):
        lines.append("## Key Concepts\n")
        lines += [f"- {c}" for c in data["concepts"]]
        lines.append("")

    if data.get("definitions"):
        lines.append("## Definitions\n")
        lines += [f"- **{d['term']}**: {d['meaning']}" for d in data["definitions"]]
        lines.append("")

    if data.get("key_facts"):
        lines.append("## Key Facts\n")
        lines += [f"- {f}" for f in data["key_facts"]]
        lines.append("")

    if data.get("exam_likely"):
        lines.append("## Likely Exam Material\n")
        lines += [f"- {e}" for e in data["exam_likely"]]
        lines.append("")

    if data.get("review_questions"):
        lines.append("## Review Questions\n")
        lines += [f"{i}. {q}" for i, q in enumerate(data["review_questions"], 1)]
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    data = summarize_text("Photosynthesis converts sunlight into energy. Chlorophyll absorbs light. It occurs in chloroplasts.", "brief")
    print(to_markdown(data, "photosynthesis_test"))


