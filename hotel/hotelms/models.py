from django.db import models
# from django.db import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.db.models.signals import pre_save
from datetime import date,timedelta,datetime
# from django.db.models import signals

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Manager(models.Model):
    name = models.CharField(max_length =100)
    cancel_booking = models.BooleanField(default=False)


    def __str__(self):
        return str(self.name)

class Room(models.Model):
    number = models.IntegerField()
    type_of_room = models.CharField(max_length=200)
    price = models.IntegerField()
    availability = models.AutoField(primary_key=True)
    no_of_beds = models.IntegerField()


    def __str__(self):
        return str(self.number)

class Guest(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    address = models.TextField()


    def __str__(self):
        return str(self.name)

class Record(models.Model):
    guest_name = models.CharField(max_length=100)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateField()
    canceling_date = models.DateField(default=date.today() + timedelta(days=8))


    def __str__(self):
        return str(self.guest_name)

# @receiver(post_save,sender =Record)
# def update_availability(sender,instance,created, **kwargs):
#     availability = instance.booking.availability
#     if not instance.canceling:
#         if instance.booking >=availability
#             availability +=1
#             booking = availability
#             if availability >0:
#                 booking = True
#             booking.save()
#
#
# @receiver(signals.pre_save,sender =Record)
# def booking(sender,instance,created,**kwargs):
#     if not instance.canceling:
#         if created:
#             availability = instance.booking.availability
#         if availability >0
#             if availability -=1
#             booking =
#



