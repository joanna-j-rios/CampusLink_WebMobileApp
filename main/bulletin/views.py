# bulletin/views.py
from django.shortcuts import render, redirect, get_object_or_404 # Import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def bulletin_board_view(request):
    form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "Post published successfully!")
                return redirect('bulletin_board')
        else:
            form = PostForm()
    
    posts = Post.objects.all().order_by('-timestamp')
    
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'bulletin/bulletin_board.html', context)

@login_required
def delete_post(request, pk):
    """
    Deletes a bulletin board post.
    Only the author of the post can delete it.
    """
    post = get_object_or_404(Post, pk=pk, author=request.user) # Ensure only author can delete
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
    return redirect('bulletin_board') # Always redirect back to the bulletin board
