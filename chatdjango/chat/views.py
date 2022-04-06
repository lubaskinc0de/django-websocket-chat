from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


#пишем контроллер главной страницы

def index(request):
    return render(request,'chat/index.html')

# пишем контроллер страницы комнаты

def room(request,room_name):
    return render(request,'chat/room.html',{
        'room_name_json': mark_safe(json.dumps(room_name)) # json.dumps это преобразование данных python в строку JSON
        #mark_safe превращает строку в безопасный html код и никак ее не экранирует
        # с mark_safe = <
        # без mark_safe = &ltk
    })
