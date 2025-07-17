from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask_ai, name='ask_ai'),
    path('response/<str:task_id>/', views.get_response, name='get_response'),
]

