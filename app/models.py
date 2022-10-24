from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_super = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)


class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'My Student'

    NONE = 'NONE'
    MATH = 'MATH'
    BIOLOGY = 'BIOLOGY'
    E_MENTOR = 'E_MENTOR'
    TEACHER = 'TEACHER'
    ENGINEER = 'ENGINEER'
    PAINTER = 'PAINTER'
    PROGRAMMER = 'PROGRAMMER'
    DOCTOR = 'DOCTOR'

    SPECIFICATIONS = [
        (NONE, 'None'),
        (MATH, 'Math'),
        (BIOLOGY, 'Biology'),
        (E_MENTOR, 'English Mentor'),
        (TEACHER, 'Teacher Global'),
        (ENGINEER, 'Engineer'),
        (PAINTER, 'Painter'),
        (PROGRAMMER, 'Programmer'),
        (DOCTOR, 'DOCTOR')
    ]

    reason = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=998)
    specification = models.CharField(
        max_length=40, choices=SPECIFICATIONS, default=NONE)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'CustomUser', related_name='students', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        
    def get_last_name(self):
        return self.first_name + ' belongs to ' + self.last_name + ' last name.'

    def __str__(self):
        return str(self.first_name)


class Sponsor(models.Model):
    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'

    NONE = 'NONE'
    JUNIOR = 'JUNIOR'
    MIDDLE = 'MIDDLE'
    SENIOR = 'SENIOR'

    DEGREE = [
        (JUNIOR, 'Junior'),
        (MIDDLE, 'Middle'),
        (SENIOR, 'Senior'),
        (NONE, 'None')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    work_degree = models.CharField(max_length=20, choices=DEGREE, default=None)
    students = models.ManyToManyField(Student, related_name='students', blank=True)
    
    # def save(self, *args, **kwargs):
    #     if self.__class__.objects.filter(student=self.students).count()>=10:
    #         return None
    #     return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['first_name']


    def __str__(self):
        return self.first_name
    
# sponsored Students
class SponsoredStudents(models.Model):
    student = models.ForeignKey(Student, blank=True, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student} and {self.sponsor}"
