# Lecture Notes Summarizer

A command line tool that turns lecture notes into structured study sheets using the Claude API. Point it at a `.txt`, `.md`, or `.pdf` file, or a whole folder, and it produces a markdown study sheet with key concepts, definitions, key facts, things that may be on the exam, and review questions.

## Features

- **Structured output**, not a flat summary — notes are organized into labeled sections
- Handles `.txt`, `.md`, and `.pdf` input
- Single file or whole folder (batch) processing
- Adjustable detail level (`brief` / `detailed`)

## Setup

```bash
git clone https://github.com/chunkychonker/lecture-notes-summarizer.git
cd lecture-notes-summarizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then copy the example env file and add your own Anthropic API key:

```bash
cp .env.example .env
```

Edit `.env` and set your key:

```
ANTHROPIC_API_KEY=your-key-here
```

## Usage

```bash
# Single file
python3 summarize.py notes/lecture1_greedy.md

# PDF input
python3 summarize.py notes/lecture1_greedy.pdf

# Whole folder, brief detail
python3 summarize.py notes/ --detail brief

# Custom output directory
python3 summarize.py notes/lecture1_greedy.md --out study-sheets
```

Study sheets are written to `output/` (or your `--out` directory) as `<name>_study.md`.

## How it works

The tool runs each file through a three stage pipeline: it reads the text (extracting from PDFs when needed), sends it to Claude with a system instruction that requests structured JSON, parses that JSON into labeled sections, and writes the result as a formatted markdown study sheet.

## Project structure

```
summarize.py        # the tool
notes/              # input notes
output/             # generated study sheets
requirements.txt    # dependencies
.env                # your API key (not committed)
.env.example        # template for the above
```

## Why I built it + What I learned

As a student, I often find myself asking LLMs to help me digest large loads of information, like lecture notes. The equations, theorems, and lemmas professors throw at you can seem pretty confusing at first, so having a tool that structures it all for you is genuinely useful. I also wanted to practice building on the Claude API by hand rather than copying generated code.

The core design decision was returning structured JSON (concepts, definitions, key facts, exam likely material, review questions) instead of a flat summary. This meant I could reliably parse and manipulate the response in Python, and it put the system instruction at the center of controlling the output. That turned out to be the biggest lesson: the quality lives almost entirely in the system prompt. A vague instruction gave mediocre results, but specifying exactly what to preserve and the exact JSON schema to return made the output reliable and consistent.

Building this taught me how to integrate with an external API end to end. I started with Gemini's Python SDK and their free model to get a grasp on how API calls work in relation to LLMs, then scaffolded from there to Anthropic's SDK (which I had to buy tokens for). I decided to use a synchronous client, since the program processes one file at a time and didn't really call for an async one. Along the way I familiarized myself with the tools and modules in the SDK, experimented with system instructions and response formatting, and learned how to manipulate those responses in Python. In the CLI context, using the os library was pretty cool, through code I could directly read and write files and folders on my laptop.














