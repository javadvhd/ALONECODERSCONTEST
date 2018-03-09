from django.db import models


class Major(models.Model):
    def __init__(self):
        short_m = models.CharField(max_length=2)
        name_m = models.CharField(max_length=20)

    short_m = models.CharField(max_length=2)
    name_m = models.CharField(max_length=20)


def make_choice():
    choice = [('CS', 'computer science')]
    objs = Major.objects.all()
    if objs:
        for obj in objs:
            choice = choice + [(obj.short_m, obj.name_m)]
    return choice


class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=20)
    Student_id = models.IntegerField()
    Name = models.CharField(max_length=50)
    last_choices = make_choice()
    major = models.CharField(max_length=2, choices=last_choices)

    def str(self):
        return repr(self.Student_id)


class Text(models.Model):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

