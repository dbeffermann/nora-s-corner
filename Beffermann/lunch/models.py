from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Employee(models.Model):
	WORKPLACE = (
			('Providencia', 'Providencia'),
			('Las Condes', 'Las Condes'),
			('Valparíso', 'Valparaíso'),
			('Viña del mar', 'Viña del mar'),
			) 
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	workplace = models.CharField(max_length=200, null=True,choices=WORKPLACE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("lunch:employee", kwargs={"id":self.id})

	def __str__(self):
		return self.name


class Dish(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	tag = models.CharField(max_length=200,null=True, blank=True)
	active = models.BooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def get_absolute_url(self):
		return reverse("lunch:dish", kwargs={"id":self.id})

	def __str__(self):
		return self.name

class Menu(models.Model):
	DAY = (
			('Monday', 'Monday'),
			('Tuesday', 'Tuesday'),
			('Wednesday', 'Wednesday'),
			('Thursday', 'Thursday'),
			('Friday' , 'Friday'),
			) 

	name = models.CharField(max_length=200, null=True)
	day = models.CharField(max_length=200, null=True, choices=DAY)
	description = models.CharField(max_length=200, null=True, blank=True)
	dishes = models.ManyToManyField(Dish)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("lunch:menu", kwargs={"id":self.id})

	def __str__(self):
		return self.name
	

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	employee = models.ForeignKey(Employee, null=True, on_delete= models.SET_NULL)
	dish = models.ForeignKey(Dish, null=True, on_delete= models.SET_NULL)
	comment = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default="Pending")

	def get_absolute_url(self):
		return reverse("lunch:order", kwargs={"id":self.id})

	def __str__(self):
		return self.employee.name



	
