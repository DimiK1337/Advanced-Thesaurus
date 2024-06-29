# Advanced Thesaurus

This project aims to create an advanced thesaurus using Natural Language Processing (NLP) and the NLTK library. It builds a lexical field tree for a given input word and prints out the tree, showing the hierarchical relationships between the words.

## Features

- Build a lexical field tree for a given word using synonyms from WordNet.
- Print the tree using ASCII characters.
- Display the depth of each node relative to its nearest root.
- Avoid redundant nodes in the tree.

## Prerequisites

- Python 3.x
- [`nltk`](https://www.nltk.org/) library
  - `wordnet` and `omw-1.4` NLTK data packages


## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/advanced-thesaurus.git
   cd advanced-thesaurus
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip3 install nltk
   ```

4. **Download NLTK data packages:**

   ```python
   import nltk
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   ```

5. **Run the main script:**

   ```bash
   python3 main.py
   ```

## Usage

1. When you run the `main.py` script, you will be prompted to enter a word.

