from django.shortcuts import render
from .form import signupforms
from django.contrib import messages
def sign_up(request):
    if request.method == 'POST':
        fm=signupforms(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully')
            fm.save()
    else:        
        fm=signupforms()
    return render(request,"enroll/signup.html",{'form':fm})

# Create your views here.
