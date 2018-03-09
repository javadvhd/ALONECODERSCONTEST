from django.db import models


class User(models.Model):
    Username = models.CharField()
    Email = models.EmailField()
    Password = models.CharField()
    Confirm_password = models.CharField()
    Student_id = models.IntegerField()
    Name = models.CharField()
    Major = models.CharField(choices=majors)

    def add_major(self, item_short, item_name):
        new_item = ((item_short, item_name),)
        self.Majors = self.Majors + new_item

    def __str__(self):
        return repr(self.Studen_id)
