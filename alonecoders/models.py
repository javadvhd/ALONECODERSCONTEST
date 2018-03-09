from django.db import models


class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=20)
    Student_id = models.IntegerField()
    Name = models.CharField(max_length=50)
    COMPUTER_ENGINEERING = 'CE'
    COMPUTER_SCIENCE = 'CS'
    MAJOR_CHOICES = (
        (COMPUTER_ENGINEERING, 'computer engineering'),
        (COMPUTER_SCIENCE, 'computer science'),
    )
    print(MAJOR_CHOICES)
    major = models.CharField(
        max_length=2,
        choices=MAJOR_CHOICES,
        default=COMPUTER_SCIENCE,
    )

    def str(self):
        return repr(self.Student_id)


class Text(models.Model):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
