from django.db import models
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=18)
    number = models.CharField(max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name

class InternShip(models.Model):
    name = models.CharField(max_length=15)
    email_address=models.EmailField()
    number=models.CharField(max_length=20)
    cover = models.CharField(max_length=20)
    resume = models.FileField()
    def __str__(self):
        return self.name
class Consult(models.Model):
    name = models.CharField(max_length=15)
    number=models.CharField(max_length=20)
    email_address=models.EmailField()
    detail = models.CharField(max_length=20)
    appoint = models.TextField()

    def __str__(self):
        return self.name

