from django.db import models
from datetime import datetime
import random

from django.db.models.fields import TimeField

# Create your models here.
def random_book_cover():
    return str(random.randint(1, 13))


class Book(models.Model):
    cover = models.CharField(max_length=2, default=random_book_cover)
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    borrow = models.DateTimeField(default=datetime.now(), blank=True)
    
    def is_borrowed(self):
        date_now = datetime.date(datetime.now())
        time_now = datetime.time(datetime.now())
        if datetime.time(self.borrow) > time_now and datetime.date(self.borrow) == date_now:
            return True
        return False

    def __str__(self):
        return self.title
