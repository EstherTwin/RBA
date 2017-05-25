from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import date
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
class Bay (models.Model):
	Bay_type_id= models.ForeignKey(Bay_type)
	Bay_Tag = models.CharField(default="3A", max_length=30)
	def __str__(self):
		return self.Bay_Tag

class Schedule(models.Model):
	Aircraft_id= models.ForeignKey(Aircraft)
	flight_id= models.ForeignKey(Flight)
	ActualDtime = models.CharField(max_length=30)
	ActualAtime= models.CharField(max_length=40)
	MPD= models.CharField(default="Armsterdam", max_length=40)
	Date = models.DateField()

	def __str__(self):
		return u'%s %s' % (self.flight_id, self.Aircraft_id)

class BayAllocation(models.Model):
	Bay_id = models.CharField(max_length=30, default="1A")
	FlightNo= models.CharField(max_length=30, default="KQ3EA")
	StartTime = models.CharField(max_length=30)
	EndTime= models.CharField(max_length=40)
	Date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return u' %s %s %s'%(self.schedule_id, self.StartTime, self.EndTime)
