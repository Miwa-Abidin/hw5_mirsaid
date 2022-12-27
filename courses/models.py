from django.db import models



class Student(models.Model):
    stud_name = models.CharField(max_length=30)
    date_birth = models.CharField(max_length=30)

    def __str__(self):
        return self.stud_name

class Mentor(models.Model):
    ment_name = models.CharField(max_length=30)
    experiense = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.ment_name} - {self.experiense}'

class Lesson(models.Model):
    name = models.CharField(max_length=30)
    course_month = models.CharField(max_length=30)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
