# bulletin/views.py

from django.shortcuts import render, redirect
from .models import Announcement

# View to show all announcements
def bulletin_home(request):
    announcements = Announcement.objects.all().order_by('-created_at')  # Get newest first
    return render(request, 'bulletin/home.html', {'announcements': announcements})

# View to post a new announcement
def post_announcement(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the form
        content = request.POST.get('content')  # Get the content from the form

        # Save the new announcement
        Announcement.objects.create(title=title, content=content)

        return redirect('bulletin_home')  # Redirect to the home page after posting

    return render(request, 'bulletin/post.html')  # If GET request, show the form
