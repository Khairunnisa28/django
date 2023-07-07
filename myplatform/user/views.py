from django.shortcuts import render
from .models import User

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})

def user_detail(request, pk):
    users = User.objects.get(pk=pk)
    return render(request, 'user/user_detail.html', {'users': users})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
