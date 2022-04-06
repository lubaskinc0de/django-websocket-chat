'''
работа с channels - асинхронностью в джанго
'''
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter # протоколы
from chat import routing

'''
настраиваем asgi аппликацию для channels
протокол тайп раутер поддерживает сразу несколько протоколов соединения
вебсокеты, http
используем вебсокет
'''

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        #authmiddlewarestack прослойка которая позволяет нам использовать сессии джанго, она просто обьединяет в себе все стандартные middleware сессии django 
        URLRouter(routing.websocket_urlpatterns) # и через UrlRouter подключаем маршруты нашего приложения chat
        )
})