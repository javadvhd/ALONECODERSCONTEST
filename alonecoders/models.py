from django.db import models


class Major(models.Model):
    short_m = models.CharField(max_length=2, default='CS')
    name_m = models.CharField(max_length=20, default='Computer Science')

    def str(self):
        return repr(self.short_m)


def add_item(base):
    return tuple(list((o.short_m, o.name_m) for o in Major.objects.all() if o not in base) + list(base))


class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=20)
    Student_id = models.IntegerField()
    Name = models.CharField(max_length=50)
    CS = 'CS'
    CE = 'CE'
    MAJOR_CHOICES = (
        (CS, 'Computer scinece'),
        (CE, 'Computer Engenier'),
    )
    MAJOR_CHOICES = add_item(MAJOR_CHOICES)
    major_in_user = models.CharField(
        max_length=2,
        choices=MAJOR_CHOICES,
        default=CS
    )

    def str(self):
        return repr(self.Student_id)


class Text(models.Model):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
