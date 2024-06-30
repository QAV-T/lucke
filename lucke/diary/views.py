from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from .models import Diary   
from .forms import DiaryForm

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('account_login')


def home(request):
    diaries = Diary.objects.filter(author=request.user).order_by('-created_at') if request.user.is_authenticated else []
    return render(request, 'diary/home.html', {'diaries': diaries})

def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    return render(request, 'accounts/signup.html')

@login_required
def create_diary(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = request.user
            diary.save()
            return redirect('profile')
    else:
        form = DiaryForm()
    return render(request, 'create_diary.html', {'form': form})


@login_required
def logout_confirmation(request):
    return render(request, 'account/logout_confirmation.html')

@login_required
def profile_view(request):
    diaries = Diary.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'diaries': diaries})

@login_required
def diary_detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, author=request.user)
    return render(request, 'diary_detail.html', {'diary': diary})

@login_required
def diary_edit(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, author=request.user)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('diary_detail', diary_id=diary.id)  
    else:
        form = DiaryForm(instance=diary)
    return render(request, 'diary_edit.html', {'form': form})

@login_required
def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, author=request.user)
    if request.method == "POST":
        diary.delete()
        return redirect('profile')
    return render(request, 'diary_delete.html', {'diary': diary})