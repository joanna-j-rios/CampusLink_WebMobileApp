# activities/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages # Keep this import for other messages
from django.http import JsonResponse
from .forms import CustomLoginForm, CustomRegistrationForm, TaskForm
from .models import Task

# --- Authentication Views ---

# This view handles both displaying the login form and processing login submissions
def login_view(request):
    # if the user is already logged in, redirect them to the home page
    if request.user.is_authenticated:
        return redirect('home')
        
    # Handle the form submission when the user clicks 'Login'.
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the user exists first.
            # if they dont prompt them to create an account
            if not User.objects.filter(username=username).exists():
                form.add_error(None, "User does not exist. Do you want to create an account?")
            # if they do...
            else:
                user = authenticate(request, username=username, password=password)
                # if they entered right password --> we found matching hash for user
                if user is not None:
                    login(request, user)
                    return redirect('home')
                # if they did not enter right password
                else:
                    form.add_error(None, "Incorrect password. Please try again.")
    else:
        form = CustomLoginForm()


    return render(request, 'activities/login.html', {'form': form})

# This view handles both displaying the registration form and creating a new user
def register_view(request):
    # if the user is already logged in, redirect them to the home page
    if request.user.is_authenticated:
        return redirect('home')
            
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # create the new user with a password
            User.objects.create_user(username=username, password=password)
            #messages.success(request, "Registration successful! You can now log in.") --> removing since we dont have messages setup in login/register html
            return redirect('login')
    else:
        form = CustomRegistrationForm()
        
    return render(request, 'activities/register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Removed: messages.info(request, "You have been logged out.")
    return redirect('login')

# --- New Home Screen View ---
@login_required
def home_view(request):
    return render(request, 'activities/home.html', {'username': request.user.username})

# --- To-Do & Planner Views ---

# --- To-Do & Planner Views ---
@login_required
def tasks_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            
            # Check for the AJAX header to handle a non-page-reloading request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return JSON with the new task data for the JavaScript to handle
                return JsonResponse({
                    'id': task.id,
                    'task_name': task.task_name,
                    'is_completed': task.is_completed,
                })
            else:
                # If it's a regular POST request, show a message and redirect as before
                messages.success(request, "Task added successfully!")
                return redirect('tasks')
    else:
        form = TaskForm()
    
    tasks = Task.objects.filter(user=request.user).order_by('is_completed', 'due_date')
    
    context = {
        'form': form,
        'tasks': tasks
    }
    return render(request, 'activities/tasks.html', context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully!")
    return redirect('tasks')

@login_required
def toggle_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
        if task.is_completed:
            messages.success(request, f"Task '{task.task_name}' marked as complete!") 
        else:
            messages.info(request, f"Task '{task.task_name}' marked as incomplete.")
    return redirect('tasks')