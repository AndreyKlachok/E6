from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *


@login_required
def index(request):
    # print(request.user)
    all_user = User.objects.all()
    # print(all_user)
    return render(request, 'chat/index.html', {'users': all_user})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def user(request, **kwargs):
    all_my_rooms = MyRooms.objects.filter(user_id=request.user.id)
    if all_my_rooms:
        for myroom in all_my_rooms:
            print(f'Room id:{myroom.id_room_id}')
            room = Room.objects.get(id=myroom.id_room_id)
            members = eval(room.members)
            if request.user.id in members and kwargs.get('pk') in members:
                print(f'Room already exists {room.name}')
                return render(request, 'chat/room.html', {'room_name': room.name})
    else:
        new_room = Room.objects.create(members=[request.user.id, kwargs.get('pk')])
        print(f'Create new room:{new_room.name}')
        MyRooms.objects.create(id_room=new_room, user=request.user)
        MyRooms.objects.create(id_room=new_room, user=User.objects.get(id=kwargs.get('pk')))
        return render(request, 'chat/room.html', {'room_name': new_room.name})
