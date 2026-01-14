from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    assigned_classes = models.ManyToManyField('courses.Course')

    def __str__(self):
        return self.full_name
