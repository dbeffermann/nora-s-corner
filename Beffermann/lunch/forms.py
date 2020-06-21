from django.forms import ModelForm
from .models import Menu, Employee, Dish, Order
from django import forms


class MenuModelForm(ModelForm):
	class Meta:
		model = Menu
		fields = '__all__'
	
class EmployeeModelForm(ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'	

class DishModelForm(ModelForm):
	class Meta:
		model = Dish
		fields = '__all__'	

class OrderModelForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'