from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Rating(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Student(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    average = models.FloatField()

