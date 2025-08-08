# views.py
from django.shortcuts import render, redirect  # Import the 'render' function to show a webpage
from .models import Announcement  # Import the Announcement model to access announcements in the database
from .forms import AnnouncementForm

# Create a view for showing the announcements
def view_announcements(request):
    # Get all announcements from the database, sorted by the most recent first
    announcements = Announcement.objects.all().order_by('-created_at')

    # Return the page to show, passing the announcements to the template
    return render(request, 'bulletin/view_announcements.html', {'announcements': announcements})

# Create a view for posting announcements
def post_announcement(request):
    if request.method == 'POST':  # If the user submits the form
        form = AnnouncementForm(request.POST)  # Get the data from the form
        if form.is_valid():  # If the form is filled out correctly
            form.save()  # Save the new announcement to the database
            return redirect('view_announcements')  # Redirect to the view_announcements page
    else:
        form = AnnouncementForm()  # Show an empty form for GET requests

    return render(request, 'bulletin/post_announcement.html', {'form': form})  # Show the form on the webpage