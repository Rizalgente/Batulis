from django.shortcuts import render
from .models import PostUser
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'dashboard.html')

def post(request):
    post = PostUser.objects.all()
    template = 'index.html'
    context = {
        'post' : post
    }
    return render(request, template, context)