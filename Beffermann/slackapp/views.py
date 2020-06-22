from django.shortcuts import render, HttpResponse, reverse, redirect
import os
from slack import WebClient
from slack.errors import SlackApiError
from django.conf import settings
import requests
from datetime import datetime, timedelta
from lunch.models import Menu
from django.views import View

# Slack Web Api base url.
BASE_URL = "https://slack.com/api/"

""" 1.- Slack Web API Methods: Users. """

def get_users(request=None):

    payload = {
        'token': settings.SLACK_OAUTH_TOKEN,
        'Content-Type': 'application/json',
        }

    response = requests.get(os.path.join(BASE_URL,'users.list/'),params=payload).json()

    obj_list = [i for i in response['members'] if not (i['name'].endswith('bot') or i['name'] == "nora")]

    if request is not None:
    
        return render(request, 'users.html', {'context': obj_list})

    else:

        return obj_list


def user_by_email(request,email=None):
    if email is not None:
        payload = {
            'token': settings.SLACK_OAUTH_TOKEN,
            'email': email
            }

        response = requests.get(os.path.join(BASE_URL, "users.lookupByEmail"), params = payload).json()

        if response['ok'] == True:

            return render(request, 'user_detail.html', {'context': response['user']})

        else:

            return redirect(reverse("slackapp:users"))



""" 2.- Slack Web API Methods: Reminders. """
def get_reminders(request):

    users = get_users()

    payload = {

        'token': settings.SLACK_OAUTH_TOKEN,

        }

    response = requests.get(os.path.join(BASE_URL, "reminders.list/"), params = payload).json()
    reminders = response['reminders']
    
    for i in reminders:
        i['time'] = datetime.fromtimestamp(int(i['time'])).strftime('%Y-%m-%d %H:%M:%S')

    for i in reminders:
        i['user'] = [user_id for user_id in users if user_id in get_users()][0]


    return render(request, 'reminders.html', {'context': reminders})


def create_reminder(request):

    model = Menu
    time = '21:34'
    menus = model.objects.all().order_by("date_created")

    if request.method == "GET":

        return render(request,'reminder_form.html', {'menus': menus})
    
    elif request.method =="POST":

        if request.POST.get('message') and request.POST.get('menu'):# and request.POST.get('time'):

            message  = str(request.POST.get('message'))
            menu_id  = request.POST.get('menu')
            menu_obj = model.objects.filter(id = menu_id)

            menu_url = request.build_absolute_uri(reverse("lunch:menu", kwargs= {"id": menu_id}))

            payload = {
                'Content-Type': 'application/json', 
                'token': settings.SLACK_OAUTH_TOKEN,
                'text': message + menu_url,
                'time': time,
                }
            
            response = requests.post(os.path.join(BASE_URL, 'reminders.add/'), params = payload)
            if response.status_code == 200:
        
                return render(request, 'reminder_form.html', {'response': response, 'success':'Reminder set, check it here: '})

            else:
                return render(request, 'reminder_form.html')


def delete_reminder(request, id=None):

    if id is not None:
        payload = {
            'token': settings.SLACK_OAUTH_TOKEN,
            'Content-Type': 'application/json',
            'reminder': id
            }

        response = requests.post(os.path.join(BASE_URL, "reminders.delete/"), params = payload).json()

        if response['ok'] == True:

            return redirect(reverse("slackapp:reminders"))
        
        else:

            return redirect(reverse("slackapp:reminders"))







""" 
class SlackView(View):

    base_url = "https://slack.com/api/"

    slack_method = 'reminders.lits/'

    template_name = 'reminders.html'

    payload = {
        'token': settings.SLACK_OAUTH_TOKEN,
        #'Content-Type': 'application/json',
    }
    
    def get(self, request, *args, **kwargs):

        #if request.method == "GET":

        response = requests.get(self.base_url + '/' + self.slack_method, params = self.payload).json()

        return render(request, self.template_name , {'context': response})

    def post(self, request, *args, **kwargs):

        #if request.method == "POST":

        response = requests.post(self.base_url + '/' + self.slack_method, params = self.payload).json()
    
        return render(request, self.template_name , {'context': response})


    

    
        



                

"""