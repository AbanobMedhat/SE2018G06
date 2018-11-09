from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=500)
    ac_year = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.ac_year


class Course(models.Model):
    name = name = models.CharField(max_length=250)
    max_degree = models.IntegerField()

    def __str__(self):
        return self.name


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    degree = models.IntegerField()

    def __str__(self):
        return str(self.degree)
