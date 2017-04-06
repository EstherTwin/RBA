from django.db import models

# Create your models here.

class Department(models.Model):
	name= models.CharField(max_length=50)

	def __str__(self):
		return self.name

class User(models.Model):
	Department_id=models.ForeignKey(Department)
	name =models.CharField(max_length=50)
	username= models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Aircraft_type(models.Model):
	Type= models.CharField(max_length=30)

	def __str__(self):
		return self.Type

class Aircraft(models.Model):
	Type_id= models.ForeignKey(Aircraft_type)
	Tag= models.CharField(max_length=70)

	def __str__(self):
		return self.Tag

class Bay_type(models.Model):
	Btype= models.CharField(max_length=50)

	def __str__(self):
		return self.Btype

class Bay(models.Model):
	Bay_type_id= models.ForeignKey(Bay_type)
	B_tag = models.CharField(max_length=30)
	Location= models.CharField(max_length=40)

	def __str__(self):
		return self.B_tag

class Schedule(models.Model):
	FlightNo= models.CharField(max_length=20)
	Aircraft_id= models.ForeignKey(Aircraft)
	Date = models.DateField()
	Arrival_time =models.CharField(max_length=10)
	Departure_time =models.CharField(max_length=10)
	Duration= models.CharField(max_length=20)

	def __str__(self):
		return u'%s %s' % (self.FlightNo, self.Aircraft_id)


