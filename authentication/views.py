from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.urls import reverse

def signin(request, error=None):
  return render(request, 'authentication/index.html', {
    'error': error
  })

def signup(request):
  return render(request, 'authentication/signup.html')

def login(request):
  if request.method == 'POST':
    user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
    print(user)
    if user is not None:
      return HttpResponseRedirect(reverse("posts:posts"))
    else:
      return redirect("authentication:signin", error='Invalid user credentials!')
  else:
    return HttpResponseBadRequest("Method not allowed!")

def register(request):
  # user = User.objects.create_user("Test User", "test.user@gmail.com", "password")
  return HttpResponse("Registering ...")
