from django.db import models

# Create your models here.

class Flight(models.Model):
	flight_No =models.CharField(max_length=50)
	source= models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	departure_time = models.CharField(max_length=50)
	arrival_time = models.CharField(max_length=50)

	def __str__(self):
		return self.flight_No

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

class Schedule(models.Model):
	Aircraft_id= models.ForeignKey(Aircraft)
	flight_id= models.ForeignKey(Flight)
	ActualDtime = models.CharField(max_length=30)
	ActualAtime= models.CharField(max_length=40)
	Date = models.DateField()

	def __str__(self):
		return u'%s %s' % (self.flight_id, self.Aircraft_id)

class BayAllocation(models.Model):
	Bay_type_id= models.ForeignKey(Bay_type)
	schedule_id= models.ForeignKey(Schedule)
	StartTime = models.CharField(max_length=30)
	EndTime= models.CharField(max_length=40)

	def __str__(self):
		return u' %s %s %s'%(self.schedule_id, self.StartTime, self.EndTime)
