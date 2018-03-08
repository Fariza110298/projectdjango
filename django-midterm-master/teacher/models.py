from django.db import models

# Create your models here.
class Teacher(models.Model):
	class Meta():
		db_table='teacher'

	teacher_firstname=models.CharField(max_length=200)
	teacher_lastname=models.CharField(max_length=200)
	teacher_subject=models.CharField(max_length=200)
	teacher_age=models.IntegerField(default=0)

class Students(models.Model):
	class Meta():
		db_table='students'

	students_firstname = models.CharField(max_length=200)
	students_lastname = models.CharField(max_length=200)
	students_course = models.IntegerField(default=0)

	students_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

