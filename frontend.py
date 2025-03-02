# frontend.py
import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = 'http://127.0.0.1:8000/review'

# Streamlit app
st.title('Automated Code Reviewer')
st.write('Upload or paste your Python code for AI-powered review.')

# Input code
code = st.text_area('Paste your Python code here:', height=300)

# File uploader
uploaded_file = st.file_uploader('Or upload a Python file:', type=['py'])
if uploaded_file is not None:
    code = uploaded_file.read().decode('utf-8')
    st.text_area('Uploaded Code:', value=code, height=300)

# Review button
if st.button('Review Code'):
    if code.strip() == '':
        st.error('Please enter some code to review.')
    else:
        with st.spinner('Reviewing code...'):
            response = requests.post(BACKEND_URL, json={'code': code})
            if response.status_code == 200:
                result = response.json()
                st.subheader('Review Results')

                # Display Syntax Check
                st.markdown('### Syntax Check')
                if 'error' in result:
                    st.error(result['error'])
                else:
                    st.success(result.get('syntax_check', 'No syntax errors found.'))

                # Display PEP8 Issues
                st.markdown('### PEP8 Issues')
                if result.get('pep8_issues'):
                    st.warning(result['pep8_issues'].replace('\n', '\n'))
                else:
                    st.success('No PEP8 issues found.')

                # Display AI Suggestions
                st.markdown('### AI Suggestions')
                st.code(result.get('ai_suggestions', 'No suggestions available.'), language='python')
            else:
                st.error(f'Error: {response.text}')