from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views import View
from .models import *
from .forms import MenuModelForm, EmployeeModelForm, DishModelForm, OrderModelForm

# Menu CRUD
class MenuCreateView(CreateView): # Create.
	model = Menu
	template_name = "lunch/menu_form.html"
	form_class = MenuModelForm
	queryset = model.objects.all()

class MenuListView(ListView): # List.
	model = Menu
	queryset = model.objects.all()
	template_name = "lunch/menu.html"

class MenuUpdateView(UpdateView): # Update.
	model = Menu
	template_name = "lunch/menu_form.html"
	form_class = MenuModelForm
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")

		return get_object_or_404(self.model, id=id_)
	
class MenuDetailView(DetailView): # Detail.
	model = Menu
	template_name = "lunch/menu_detail.html"

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

class MenuDeleteView(DeleteView): # Delete.
	model = Menu
	template_name = "lunch/menu_delete.html"

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

	def get_success_url(self):
		return reverse('lunch:menus')


# Employee CRUD
class EmployeeCreateView(CreateView): # Create.
	model = Employee
	template_name = "lunch/employee_form.html"
	form_class = EmployeeModelForm
	queryset = model.objects.all()

class EmployeeListView(ListView): # List.
	model = Employee
	queryset = model.objects.all()
	template_name = "lunch/employee.html"

class EmployeeUpdateView(UpdateView): # Update.
	model = Employee
	template_name = "lunch/employee_form.html"
	form_class = EmployeeModelForm
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")

		return get_object_or_404(self.model, id=id_)
	
class EmployeeDetailView(DetailView): # Detail.
	model = Employee
	template_name = "lunch/employee_detail.html"
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

class EmployeeDeleteView(DeleteView): # Delete.
	model = Employee
	template_name = "lunch/employee_delete.html"

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

	def get_success_url(self):
		return reverse('lunch:employees')


# Dish CRUD
class DishCreateView(CreateView): # Create.
	model = Dish
	template_name = "lunch/dish_form.html"
	form_class = DishModelForm
	queryset = model.objects.all()

class DishListView(ListView): # List.
	model = Dish
	queryset = model.objects.all()
	template_name = "lunch/dish.html"

class DishUpdateView(UpdateView): # Update.
	model = Dish
	template_name = "lunch/dish_form.html"
	form_class = DishModelForm
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")

		return get_object_or_404(self.model, id=id_)

class DishDetailView(DetailView): # Detail.
	model = Dish
	template_name = "lunch/dish_detail.html"
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

class DishDeleteView(DeleteView): # Delete.
	model = Dish
	template_name = "lunch/dish_delete.html"

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

	def get_success_url(self):
		return reverse('lunch:dishes')


# Order CRUD
class OrderCreateView(CreateView): # Create.
	model = Order
	template_name = "lunch/order_form.html"
	form_class = OrderModelForm
	queryset = model.objects.all()

class OrderListView(ListView): # List.
	model = Order
	queryset = model.objects.all()
	template_name = "lunch/order.html"

class OrderUpdateView(UpdateView): # Update.
	model = Order
	template_name = "lunch/order_form.html"
	form_class = OrderModelForm
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")

		return get_object_or_404(self.model, id=id_)

class OrderDetailView(DetailView): # Detail.
	model = Order
	template_name = "lunch/order_detail.html"
	queryset = model.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

class OrderDeleteView(DeleteView): # Delete.
	model = Order
	template_name = "lunch/order_delete.html"

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(self.model.objects.filter(id=id_))

		return obj

	def get_success_url(self):
		return reverse('lunch:orders')


# Home Dashboard.
def home(request):
	orders = Order.objects.all()
	employees = Employee.objects.all()
	template_name = 'lunch/dashboard.html'
	total_orders = orders.count()
	on_delivery = orders.filter(status='Out for delivery')
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'employees':employees,
		'total_orders':total_orders,'on_delivery':on_delivery,
		'delivered':delivered,'pending':pending }

	return render(request, 'lunch/dashboard.html', context)
"""
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.html',context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/menu_create.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)
	"""