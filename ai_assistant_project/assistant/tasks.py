from celery import shared_task
import openai
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

@shared_task
def get_ai_response(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        top_p=1.0
    )

    return response['choices'][0]['message']['content']
