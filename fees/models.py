from django.db import models
from students.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

