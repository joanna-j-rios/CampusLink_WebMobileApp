# activities/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages # Keep this import for other messages

from .forms import CustomLoginForm, CustomRegistrationForm, TaskForm
from .models import Task

# --- Authentication Views ---

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    # Initialize form here so it's always defined for both POST and GET requests.
    # If it's a POST, it will be re-assigned with request.POST data.
    form = CustomLoginForm() 

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Removed: messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.") # Keep this for error messages
        # No 'else' needed here, as the form variable is already defined and passed below.
    # No 'else' block for the form initialization here, as it's done at the beginning.

    return render(request, 'activities/login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
            
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful! You can now log in.") # Keep this message
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

@login_required
def tasks_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully!") # Keep this message
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
        messages.success(request, "Task deleted successfully!") # Keep this message
    return redirect('tasks')

@login_required
def toggle_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
        # You can choose to keep or remove these specific messages for toggling task status
        if task.is_completed:
            messages.success(request, f"Task '{task.task_name}' marked as complete!") 
        else:
            messages.info(request, f"Task '{task.task_name}' marked as incomplete.")
    return redirect('tasks')
