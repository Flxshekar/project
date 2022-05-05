from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'index.html')

def pages(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass1']
        print(username)
        print(password)
        return redirect('home')
    return render(request,'pages.html')