# 🤖 AI Assistant for Telling a joke

This project is a Django-based AI Assistant system with Celery for background processing and OpenAI for AI-powered responses.

---

## Key Features

- ✨ Ask AI questions via web API (`/assistant/ask/`)
- ⏱️ Background processing with Celery + Redis
- 🧠 OpenAI integration for intelligent responses

---

## Getting Started

###  1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-assistant.git
cd ai-assistant

---

✅ 2. Set Up Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

✅ 3. Add Environment Variables
Create a `.env` file in the root directory with your OpenAI key:
.env
OPENAI_API_KEY=your-openai-api-key-here

✅ 4. Start Redis
Option A: If Redis is installed locally
redis-server

Option B: Using Docker
docker run -d -p 6379:6379 redis

✅ 5. Start Django Server
python manage.py runserver

✅ 6. Start Celery Worker (in a second terminal)
celery -A ai_assistant_project worker --loglevel=info

✅ Using the Assistant

# Ask the AI a question (returns task ID)
curl "http://localhost:8000/assistant/ask/?prompt=Tell%20me%20a%20joke"

# Poll for the response (replace <task_id> with actual ID from previous step)
curl "http://localhost:8000/assistant/response/<task_id>"


