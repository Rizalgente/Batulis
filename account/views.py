from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from .forms import CreateUserForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login, logout

def daftar(request):
    template = render_to_string('aktivasi_email.html', {'name':request.user.first_name})
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # form.is_active = False
            form.save()

            # email = EmailMessage(
            #     'Terima kasih telah mendaftar di Batulis.com',
            #     template,
            #     settings.EMAIL_HOST_USER,
            #     [request.user.email],
            # )
            # email.fail_silently = False
            # email.send()

            # user = form.cleaned_data.get('username')
            return redirect('login')
        else:
            messages.error(request,"terjadi kesalan!")
    context = {'form' : form}
    
    return render(request, 'daftar.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,"username atau password salah!")
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    
def kirim(request):
    return render(request,'aktivasi_email.html')


