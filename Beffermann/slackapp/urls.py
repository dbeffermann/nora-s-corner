from django.urls import path
from . import views

app_name = "slackapp"
urlpatterns = [
    #path('', views.slackmessage, name = "slackapp"),
    path('reminders/', views.get_reminders, name = "reminders"),
    path('reminder/create/', views.create_reminder, name = "reminder_create"),
    path('reminder/<str:id>/delete/', views.delete_reminder, name = "reminder_delete"),

    path('users/', views.get_users, name='users'),
    path('user/by_email/<str:email>/',views.user_by_email, name='user_by_email')
    
    #path('slackappp/', views.SlackView.as_view(), name="slackapp_"),
    #path('misreminderss/', views.MisReminders.as_view(), name="misreminderss")
]