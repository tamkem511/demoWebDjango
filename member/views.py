from django.shortcuts import render,redirect
from django.views import View
from .forms import formUser,formLogin
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class addUser(View):
    def get(self, request):
        Data = {'user':formUser}
        return render(request,'member/index.html',Data)
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('save successful')

class loginUser(View):
    def get(self, request):
        Data = {'Fl':formLogin}
        return render(request, 'member/login.html',Data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if(user is not None):
            login(request,user)
            return render(request, 'member/homePage.html')
        else:
            return HttpResponse('error')

def logOut(request):
    logout(request)
    return redirect('member:login')

class homePage(LoginRequiredMixin,View):
    login_url='/member/login/'
    # redirect_field_name = 'redirect_to'
    def get(self, request):
        return render(request, 'member/homePage.html')

