from django.db import models
class Student(models.Model):
    student_id = models.IntegerField()
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    textbook_version = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateField()

    def __str__(self):
        return f'{self.student_id} - {self.province}, {self.city}'
