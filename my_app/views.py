from django.shortcuts import render, redirect
from .forms import UserRegistrationForm , PostForm
from django.contrib.auth import authenticate ,login,logout
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse

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
    post_list = Post.objects.all().order_by('updated_at')  #select * from post order
    return render(request, 'display-post.html',{'post_list':post_list})
        
def register(request):
 form = UserRegistrationForm()           # it will create a empty registration form 
 if request.method =='GET':
         return render(request,'register.html',{'form':form})
 if request.method =='POST':
        # request.POST contains data
        form = UserRegistrationForm(request.POST)   # form filled with userdata

def read_post(request, id):
    try:
           post = Post.objects.get(pk=id) #get single  record based on id 
    except Post.DoesNotExist:
      return redirect('display-post')
    
    return render(request, 'read-post.html',{'post':post})

def add_post(request):
    form = PostForm() #empty postform
    if request.method == 'GET':
        return render(request,'add-post.html',{'form':form})


    if request.method == 'POST':
        #request.post contains from data
         form = PostForm(request.POST , request.FILES)  
         if form.is_valid():
             post = form.save(commit=False)  
             post.author =  request.user  #assign user as author
             post.save() #create post
             return redirect('display-post')
         else:
             return render(request,'add-post.html', {'form':form})

@login_required(login_url='login')       
def update_post(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExists:
     return redirect ('display-post')
    if request.user != post.author:
        return HttpResponse('unauthorized access!')
    
    form = PostForm(instance=post)

    if request.method == 'GET':
        return render(request,'update-post.html',{'form': form})

    if request.method == 'POST':
      form = PostForm(request.POST,request.FILES, instance=post)    

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.updated_at = timezone.now() 
        post.save()
        form = PostForm()
        
        return redirect('display-post')
    else:
        return render(request,'update-post.html',{'form': form})
    
def delete_post(request, id):
    try:
        post = Post.objects.get(pk=id)
    except post.DoesNotExists:
        return redirect('display-post') 
    if request.user != post.author:
        return redirect('display-post')
    
    post.delete()
    return redirect('display-post')
