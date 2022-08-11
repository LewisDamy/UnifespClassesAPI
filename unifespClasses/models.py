from django.db import models

# Create your models here.

class Subject(models.Model):
    subjectID = models.AutoField(primary_key=True)
    subjectName = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    chTotal = models.IntegerField()
    requirements = models.CharField(max_length=300)
    semesterAvailable = models.CharField(max_length=50)

# class Semester(models.Model):
#     # TODO
#
# class CourseFocus(models.Model):
#     # TODO
#
# class AmountCredits(models.Model):
#     # TODO
#     chTotal = models.IntegerField()
#
# class SubjectDetail(models.Model):
#     # TODO
#     # id = models.AutField(primary_key=True)    # Inherit form Subject the id & SubjectName
#     description = models.CharField(max_length=5000)
