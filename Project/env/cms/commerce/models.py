from django.db import models




# Create your models here.
class Laptop(models.Model):
	name = models.CharField(max_length=200)
	storage = models.CharField(max_length=200)
	screen_size = models.CharField(max_length=200)
	OS = models.CharField(max_length=200)
	RAM = models.CharField(max_length=200)
	Processor = models.CharField(max_length=200)
	Warranty = models.CharField(max_length=200)
	Price = models.FloatField(max_length=10,default=0)

	def __str__(self):
		return self.name
