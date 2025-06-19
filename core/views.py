from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Get all users with the same email, ordered by date_joined (oldest first)
            users = User.objects.filter(email=email).order_by('date_joined')

            if users.exists():
                # Pick the first user (oldest)
                user = users.first()

                # Authenticate the user using username and password
                user = authenticate(request, username=user.username, password=password)

                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'core/login.html', {'error': 'Invalid Credentials'})
            else:
                return render(request, 'core/login.html', {'error': 'User not found. Please Register'})

        except User.DoesNotExist:
            return render(request, 'core/login.html', {'error': 'User not found. Please Register'})

    return render(request, 'core/login.html')


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def custom_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)

            # Important fix here:
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            login(request, user)
            return redirect('home')
        else:
            # Username already exists
            return render(request, 'core/register.html', {'error': 'Username already exists.'})

    return render(request, 'core/register.html')


@login_required
def home(request):
    return render(request, 'core/home.html')

def custom_logout(request):
    logout(request)
    return redirect('login')


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')

