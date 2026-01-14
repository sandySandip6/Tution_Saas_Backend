from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
