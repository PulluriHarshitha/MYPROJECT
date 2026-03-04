from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.
#1)functions    2)class

def home(request):
    name = 'Harshitha'
    fruits = ['apple','mango','banana','grapes']
    context = {'name': name , 'fruits':fruits}
    
    return render(request, 'home.html',context)


def user_login(request):
    return render(request, 'login.html')

def register(request):
    form = UserRegistrationForm()  #empty registration form

    if request.method == 'GET':
       return render(request, 'register.html',{'form':form})
    
    if request.method == 'POST':
        #request.POST contains from data
        form = UserRegistrationForm(request.POST) #form filled with user data

        if form.is_valid():
            form.save() #create user
            return  redirect('login')
        else:
            return render(request, 'register.html', {'form':form})
        
    
