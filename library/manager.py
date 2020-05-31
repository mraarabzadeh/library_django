from django.db import models
import datetime


class AllBook(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()#raw('select * from library_book')


class LibraryAdminBookDeliverd(models.Manager):
    def get_queryset(self, student_id):
        return super().get_queryset().get(pk=student_id)


class TimeDeliverdBook(models.Manager):
    def get_queryset(self, start, end):
        return super().get_queryset().filter(start_time__gt=start, end_time__lt=end)


class UserDidNotGetBook(models.Manager):
    def get_queryset(self):
        return super().get_queryset().raw(
            'select * from library_user u WHERE u.university_id not in \
            (select r.reserver_id from library_reservehistory r)'
        )


class UserLoveSpecialWrite(models.Manager):
    def get_queryset(self):
        return super().get_queryset().raw(
            'select u.username, u.email from library_user u, library_reservehistory r1, library_reservehistory r2,\
             library_book b1,library_book b2 where r1.reserver_id = r2.reserver_id and \
             r1.book_id = b1.id and r2.book_id = b2.id and r1!=r2 and u.university_id = r1.reserver_id'
        )


class ExpieringReserve(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end_time__lt=datetime.datetime.now() + 2)


class ReservedSpecialBookYear(models.Manager):
    def get_queryset(self, year):
        return super().get_queryset().filter(year=year)



