# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomLoginForm, CustomRegistrationForm
from .models import Task

# Create your views here.



# This view handles both displaying the login form and processing login submissions.
def login_view(request):
    # If the user is already logged in, redirect them to the tasks page.
    if request.user.is_authenticated:
        return redirect('tasks')
        
    # Handle the form submission when the user clicks 'Login'.
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the user exists first.
            if not User.objects.filter(username=username).exists():
                form.add_error(None, "User does not exist. Do you want to create an account?")
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('tasks')
                else:
                    form.add_error(None, "Incorrect password. Please try again.")
    else:
        form = CustomLoginForm()

    return render(request, 'activities/login.html', {'form': form})




# This view handles both displaying the registration form and creating a new user.
def register_view(request):
    # If the user is already logged in, redirect them to the tasks page.
    if request.user.is_authenticated:
        return redirect('tasks')
        
    # Handle the form submission when the user clicks 'Register'.
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Create the new user with a password.
            User.objects.create_user(username=username, password=password)
            
            # Log the new user in and redirect them.
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('tasks')
    else:
        form = CustomRegistrationForm()
        
    return render(request, 'activities/register.html', {'form': form})




# This view logs the user out.
def logout_view(request):
    logout(request)
    return redirect('login')





# This view to displays the tasks for the current user

# note: @login_required is built in Django decorator that ensures only a logged-in
# user can access this page. If a user tries to access it without it being logged-in
# they will be redirected to the login page

@login_required
def tasks_view(request):
    # Retrieve all tasks for the currently logged-in user
    tasks = Task.objects.filter(user=request.user).order_by('is_completed', 'due_date')
    
    # Context is a dictionary that holds the data to be passed to the template
    context = {
        'tasks': tasks,
    }
    
    # Render the HTML template and pass the tasks data to it
    return render(request, 'activities/tasks.html', context)
