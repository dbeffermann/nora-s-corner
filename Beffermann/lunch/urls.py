from django.urls import path
from . import views

app_name = "lunch"
urlpatterns = [
    path('', views.home, name="home"),

    # Menu CRUD
    path('menus/', views.MenuListView.as_view(), name='menus'),
    path('menu/create/', views.MenuCreateView.as_view(), name='menu_create'),
    path('menu/<int:id>/', views.MenuDetailView.as_view(), name='menu'),
    path('menu/<int:id>/update/', views.MenuUpdateView.as_view(), name='menu_update'),
    path('menu/<int:id>/delete/', views.MenuDeleteView.as_view(), name='menu_delete'),
    # Employee CRUD
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:id>/', views.EmployeeDetailView.as_view(), name='employee'),
    path('employee/<int:id>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:id>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    #Dish CRUD
    path('dishes/', views.DishListView.as_view(), name='dishes'),
    path('dish/create/', views.DishCreateView.as_view(), name='dish_create'),
    path('dish/<int:id>/', views.DishDetailView.as_view(), name='dish'),
    path('dish/<int:id>/update/', views.DishUpdateView.as_view(), name='dish_update'),
    path('dish/<int:id>/delete/', views.DishDeleteView.as_view(), name='dish_delete'),
    #Order CRUD
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<int:id>/', views.OrderDetailView.as_view(), name='order'),
    path('order/<int:id>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:id>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
    

    
    #path('menu/<int:id>/delete/', views.MenuDetailView.as_view(), name='menu_delete'),

    #path('customer/<str:pk_test>/', views.customer, name="customer"),
    #path('create_order/', views.createOrder, name="create_order"),
    #path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    #path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]