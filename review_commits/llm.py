import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def review_commit(commit_message, commit_hash, author, date):
    response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        },

        data=json.dumps({
            "model": "openai/gpt-oss-120b:free",
            "messages": [
                {
                    "role": "user",
                    "content": f"""Review this git commit message and respond only in JSON
Commit: {commit_hash}
Author: {author}
Date: {date}
Message: {commit_message}

Return this exact structure:
{{
    "rating": "excellent | good | bad",
    "reasoning": "<give a brief reasoning/explanation for why you chose the rating you gave it>" 
}}"""
                }
            ]
        }) 
    )

    result = response.json()
    content = result['choices'][0]['message']['content']

    try:
        return json.loads(content)
    except json.JSONDecodeError:   
        return {"rating": "N/A", "reasoning": content}
