from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'aggregator/index.html')

#---------- Auth Stuff ----------#
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'ecommerce/user/account.html')
        else:
            return render(request, 'aggregator/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'aggregator/login.html')