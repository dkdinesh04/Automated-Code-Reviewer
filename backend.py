# backend.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import subprocess
import os
import torch
import logging
from typing import Dict, Any

# Initialize FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load Hugging Face CodeGen model and tokenizer
MODEL_NAME = 'Salesforce/codegen-350M-mono'
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    raise RuntimeError(f"Failed to load model: {str(e)}")

# Pydantic model for request body
class CodeReviewRequest(BaseModel):
    code: str

# Function to check syntax errors
def check_syntax(code: str) -> Dict[str, Any]:
    try:
        compile(code, '<string>', 'exec')
        return {'syntax_check': 'No syntax errors found.'}
    except SyntaxError as e:
        return {'error': f'Syntax Error: {str(e)}'}

# Function to check PEP8 compliance
def check_pep8(code: str) -> str:
    with open('temp_code.py', 'w') as f:
        f.write(code)
    try:
        flake8_output = subprocess.run(['flake8', 'temp_code.py'], capture_output=True, text=True)
        return flake8_output.stdout if flake8_output.stdout else 'No PEP8 issues found.'
    except Exception as e:
        return f'PEP8 Check Error: {str(e)}'
    finally:
        os.remove('temp_code.py')

# Function to generate AI-powered suggestions
def get_ai_suggestions(code: str) -> str:
    try:
        input_text = f'Review the following Python code for syntax errors, logical errors, and best practices. Provide detailed suggestions for improvement:\n\n{code}\n\nSuggestions:'
        inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=512, num_return_sequences=1, temperature=0.7, do_sample=True)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f'AI Suggestion Error: {str(e)}'

# API endpoint for code review
@app.post('/review')
async def review_code(request: CodeReviewRequest) -> Dict[str, Any]:
    code = request.code
    syntax_result = check_syntax(code)
    if 'error' in syntax_result:
        return syntax_result
    pep8_issues = check_pep8(code)
    ai_suggestions = get_ai_suggestions(code)
    return {
        'syntax_check': syntax_result['syntax_check'],
        'pep8_issues': pep8_issues,
        'ai_suggestions': ai_suggestions,
    }

# Run the FastAPI app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)