from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate ,login,logout
from .models import Post
# Create your views here.
#1)functions    2)class

def home(request):
    name = 'Harshitha'
    fruits = ['apple','mango','banana','grapes']
    context = {'name': name , 'fruits':fruits}
    
    return render(request, 'home.html',context)

def user_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':          # after form  submission
        #request.POST contaion form data

        username =request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request,username=username,password=password) 

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
          error ='invalid username or password'
          return render(request,'login.html',{'error':error})
        
def user_logout(request):
    logout(request)
    return redirect('home')

def display_post(request):
    post_list = Post.objects.all()  #select * from
    return redirect(request, 'display-post.html'),{'post_list':post_list}
        
def register(request):
 form = UserRegistrationForm()           # it will create a empty registration form 
 if request.method =='GET':
         return render(request,'register.html',{'form':form})
 if request.method =='POST':
        # request.POST contains data
        form = UserRegistrationForm(request.POST)   # form filled with userdata

        