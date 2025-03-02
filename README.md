# Automated Code Reviewer

## Project Overview
The Automated Code Reviewer is a tool that uses advanced AI models like OpenAI Codex or Hugging Face's CodeGen to automatically review Python code for syntax errors, logic errors, and best practices. This project aims to streamline the code review process, providing developers with instant feedback and suggestions for improvement.

## Key Features
- **Syntax Checking:** Detects syntax errors in the Python code.
- **PEP8 Compliance:** Checks for style and formatting issues according to PEP8 guidelines.
- **AI-Powered Suggestions:** Utilizes generative models to provide detailed suggestions to improve the code.
- **User Interface:** Simple and intuitive UI using Streamlit.
- **Backend with FastAPI:** Efficient request handling and processing.

## Tech Stack
- **Programming Language:** Python
- **Libraries:**
  - `transformers` (Hugging Face)
  - `torch` (for model inference)
  - `streamlit` (UI)
  - `fastapi` (Backend)
  - `flake8` (PEP8 compliance check)
- **Deployment:** FastAPI, Uvicorn

## Installation
```sh
# Clone the repository
git clone https://github.com/your-repo/automated-code-reviewer.git
cd automated-code-reviewer

# Create a virtual environment
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
uvicorn backend:app --reload

# Run the Streamlit frontend
streamlit run frontend.py
```

## Usage
1. Paste your Python code in the text area or upload a `.py` file.
2. Click on 'Review Code'.
3. View syntax errors, PEP8 issues, and AI suggestions.

## Example
```python
# Example code to review
import os
print(os.getcwd())
```

## Evaluation Criteria
- **Functionality:** Does the project work as intended?
- **Code Quality:** Readability, modularity, and documentation.
- **GenAI Integration:** Effective use of generative models.
- **Creativity:** Unique problem-solving or UI design.
- **Scalability:** Ability to handle real-world data.
