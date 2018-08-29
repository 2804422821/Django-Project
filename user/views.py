from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.

@login_required()
def login(request):
    if request.method == "GET":
        return render('login.html')

    else:
        userForm = request.POST
        username = userForm.username
        password = userForm.password
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return render(request, "index.html")