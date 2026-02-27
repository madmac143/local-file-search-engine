# Local File Search Engine (Python)

A modular, backend-focused search engine that scans local directories, extracts text from multiple file types, indexes the content, and returns ranked search results. This project is built to show real backend fundamentals: parsing, indexing, ranking, modular architecture, and future GUI expansion.

---

## What this project does

This search engine walks through a directory, pulls text out of supported files, breaks that text down into searchable tokens, builds an index, and lets you run queries against it. The goal is to keep the architecture clean and easy to extend — something that can grow into a full desktop app later.

Current capabilities include:
- plain text file support  
- `.docx` extraction  
- PDF extraction  
- tokenization  
- indexing  
- ranking  
- query parsing  
- a simple command-line interface  

A GUI is planned next.

---

## Why I built it

I wanted a project that wasn’t just “another CRUD app.” This one shows real engineering fundamentals: file handling, modular design, search logic, and the kind of architecture you can build on top of. It’s also something I can keep improving as my skills grow — adding a GUI, better ranking, fuzzy search, caching, etc.

---

## Features

- **Directory scanning** — walks through folders and collects supported files  
- **Text extraction** — pulls text from `.txt`, `.docx`, and PDF files  
- **Tokenization** — cleans and tokenizes text  
- **Indexing** — builds an inverted index for fast lookups  
- **Query parsing** — handles multi-word queries and operators  
- **Ranking** — basic scoring system for relevance  
- **Modular architecture** — each part lives in its own file for clarity  
- **Future GUI support** — designed to plug into a Tkinter or PyQt interface  

---

## Project structure

Each module handles one job. This keeps the code readable and makes it easy to upgrade individual parts later.

file_search_engine/
│
├── scanner.py          # Walks directories and finds files
├── extractor.py        # Extracts text from txt/docx/pdf
├── tokenizer.py        # Cleans and tokenizes text
├── indexer.py          # Builds the inverted index
├── query_parser.py     # Parses user queries
├── rank.py             # Scores and ranks results
├── search_engine.py    # Orchestrates the search pipeline
├── search.py           # Search interface logic
└── main.py             # CLI entry point


---

## How to run it

1. Clone the repo:  
   `git clone https://github.com/madmac143/local-file-search-engine.git`

2. Install dependencies:  
   (You’ll need `python-docx` and `PyPDF2`)

3. Run the CLI:  
   `python3 main.py`

4. Enter the directory you want to index and start searching.

---

## Roadmap

This project is built to grow. Here’s what’s coming next:

- GUI (Tkinter or PyQt)  
- BM25 ranking  
- Fuzzy search  
- Incremental indexing  
- File previews  
- Search history  
- Settings panel  
- Better PDF extraction  
- Async scanning for large directories  

---

## What this project shows (for portfolio reviewers)

- Clean, modular Python architecture  
- Ability to design and build a full backend system  
- Understanding of indexing, parsing, and ranking  
- Real-world file handling  
- Planning for scalability and future features  
- Clear documentation and version control  

This project demonstrates actual engineering thinking, not just tutorial-level code.
