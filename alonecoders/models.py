from django.db import models


class Major(models.Model):
    majors = (('CS', 'Computer Science'), )
    Major = models.CharField(max_length=2, choices=majors, default='')

    def add_major(self, item_short, item_name):
        new_item = ((item_short, item_name),)
        self.Majors = self.Majors + new_item


class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=20)
    Student_id = models.IntegerField()
    Name = models.CharField(max_length=50)
    Major = models.ForeignKey(Major, on_delete=models)

    def __str__(self):
        return repr(self.Student_id)


