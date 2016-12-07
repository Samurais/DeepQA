from django.conf.urls import url
from . import views

from .chatbotmanager import ChatbotManager

urlpatterns = [
    url(r'api/v1/question', views.question)
]
