from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from .models import Post
from .forms import PostForm

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('account_login')


def home(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at') if request.user.is_authenticated else []
    return render(request, 'diary/home.html', {'posts': posts})

def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    return render(request, 'accounts/signup.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')