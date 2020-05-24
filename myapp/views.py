from django.shortcuts import render
from myapp import forms
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def register(request):
    if request.method=="POST":
        password=request.POST.get('password')
        userform=forms.UserRegistration(request.POST)
        if userform.is_valid():
            user=userform.save(commit=False)
            user.set_password(password)
            user.save()
            return render(request,'myapp/success.html')
    form=forms.UserRegistration()
    return render(request,'myapp/register.html',{'form':form})
