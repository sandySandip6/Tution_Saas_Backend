import uuid
from django.db import models


class Student(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    student_code = models.CharField(max_length=20, unique=True)

    
    STUDENT_STATUS = [
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('expelled', 'Expelled'),
        ('transferred', 'Transferred'),
        ('graduated', 'Graduated'),
    ]
    status = models.CharField(max_length=15, choices=STUDENT_STATUS)
    # grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    enrollment_date = models.DateField()

    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=15)
    guardian_email = models.EmailField(null=True, blank=True)
    guardian_relation = models.CharField(max_length=20)

    address = models.TextField()

    
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
