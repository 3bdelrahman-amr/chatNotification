from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from notifications.signals import notify


def index(request):
    try:
        users = User.objects.all()
        print(request.user)
        print(users)
        user = User.objects.get(username=request.user)
        notifications=user.notifications.filter()
      
        return render(request, 'index.html', {'users': users, 'user': user,'notifications':notifications})
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site as admin for sending messages.")


def message(request):
    try:
        if request.method == 'POST':
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(id=request.POST.get('user_id'))
            print(request.POST.get('message'))
            notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('index')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")






#from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Board
#def home(request):
#   boards = Board.objects.all()
#   return render(request, 'home.html', {'boards': boards})
