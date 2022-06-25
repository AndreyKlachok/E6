import uuid
from django.db import models
from django.contrib.auth.models import User


def get_uuid():
    id = uuid.uuid4().hex
    print(id)
    return str(id)


class Room(models.Model):
    name = models.TextField(default=get_uuid())
    members = models.TextField()


class MyRooms(models.Model):
    id_room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# python manage.py shell
# from chat.models import *
