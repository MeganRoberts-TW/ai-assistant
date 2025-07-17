from django.http import JsonResponse
from celery.result import AsyncResult
from ai_assistant_project.celery import app
from .tasks import get_ai_response


def ask_ai(request):
    prompt = request.GET.get('prompt', '')

    if not prompt:
        return JsonResponse({'error': 'No prompt provided'}, status=400)

    task = get_ai_response.delay(prompt)
    return JsonResponse({'task_id': task.id})

def get_response(request, task_id):
    task_result = AsyncResult(task_id, app=app)

    if task_result.state == 'PENDING':
        return JsonResponse({'status': 'pending'})

    elif task_result.state == 'SUCCESS':
        return JsonResponse({'status': 'done', 'response': task_result.result})

    elif task_result.state == 'FAILURE':
        return JsonResponse({'status': 'failed', 'error': str(task_result.result)})

    return JsonResponse({'status': task_result.state})
