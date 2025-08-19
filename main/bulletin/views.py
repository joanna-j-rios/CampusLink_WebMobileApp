# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def bulletin_board_view(request):
    """
    Renders the bulletin board page.
    """
    return render(request, 'bulletin/bulletin_board.html')
