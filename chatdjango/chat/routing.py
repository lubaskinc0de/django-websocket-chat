from django.urls import path
from . import consumers

# настраиваем маршруты для приложения chat
websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer) # маршрут для подключения вебсокета, в качевстве view выступает chatconsumer в consumers.py
]