from dotenv import load_dotenv
load_dotenv()

import argparse
import glob


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
    raw = response.content[0].text.strip()
    raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
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

def process_file(path, detail, out_dir):
    text = read_file_text(path)

    if not text.strip():
        print(f"  skipped (empty): {path}")
        return

    name = os.path.splitext(os.path.basename(path))[0]
    print(f"  summarizing: {name} ...")

    data = summarize_text(text, detail)
    markdown = to_markdown(data, name)

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{name}_study.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"  wrote: {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Turn lecture notes into structured study sheets.")
    parser.add_argument("input", help="A notes file, or a folder of notes files.")
    parser.add_argument("--detail", choices=["brief", "detailed"], default="detailed")
    parser.add_argument("--out", default="output", help="Output directory.")
    args = parser.parse_args()

    if os.path.isdir(args.input):
        files = glob.glob(os.path.join(args.input, "*.txt")) + \
                glob.glob(os.path.join(args.input, "*.md")) + \
                glob.glob(os.path.join(args.input, "*.pdf"))
        if not files:
            print("No notes files found in folder.")
            return
        print(f"Found {len(files)} file(s).")
        for path in files:
            process_file(path, args.detail, args.out)
    else:
        process_file(args.input, args.detail, args.out)


if __name__ == "__main__":
    main()    

