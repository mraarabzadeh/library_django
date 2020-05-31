from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from library.manager import *


class User(AbstractUser):
    university_id = models.IntegerField(primary_key=True)
    DidNotGetBook = UserDidNotGetBook()
    LovedWriter = UserLoveSpecialWrite()
    object = models.Manager()


class Book(models.Model):
    writer = models.CharField(max_length=120, null=False)
    translator = models.CharField(max_length=120, null=True)
    shabak = models.CharField(max_length=120, null=False)
    year = models.TimeField()
    title = models.CharField(max_length=120, null=False)
    number = models.IntegerField(null=False, default=1)
    number_of_reserved = models.IntegerField(null=False, default=0)
    AllBook = AllBook()
    object = models.Manager()

    def __str__(self):
        return '{} {} {} {}'.format(self.title, self.translator, self.writer, self.shabak)


class LibraryAdmin(models.Model):
    id = models.ForeignKey(to=User, primary_key=True, on_delete=CASCADE)
    MostDeliver = LibraryAdminBookDeliverd()
    object = models.Manager()


class ReserveHistory(models.Model):
    reserver = models.ForeignKey(to=User, on_delete=CASCADE)
    admiter = models.ForeignKey(to=LibraryAdmin, on_delete=CASCADE)
    book = models.ForeignKey(to=Book, on_delete=CASCADE)
    start_time = models.DateTimeField(null=False, default=datetime.datetime.now())
    end_time = models.DateTimeField(null=False)
    ReservedBookSpecialTimeRange = TimeDeliverdBook()
    ExpieringReserve = ExpieringReserve()
    SpecialYearReservation = ReservedSpecialBookYear()
    object = models.Manager()
