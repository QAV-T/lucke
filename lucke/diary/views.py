from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView
from django.http import JsonResponse
from .models import Diary, Sidenote  
from .forms import DiaryForm, SidenoteForm
from django.template.loader import render_to_string



class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('account_login')

class CustomLoginView(LoginView):
    template_name = 'login.html' 
    redirect_authenticated_user = True  

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



def home(request):
    diaries = Diary.objects.filter(author=request.user).order_by('-created_at') if request.user.is_authenticated else []
    return render(request, 'diary/home.html', {'diaries': diaries})

def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    return render(request, 'accounts/signup.html')

def about(request):
    return render(request, 'about.html')

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
    sidenotes = Sidenote.objects.filter(diary=diary).order_by('created_at')
    
    if request.method == 'POST':
        form = SidenoteForm(request.POST)
        if form.is_valid():
            sidenote = form.save(commit=False)
            sidenote.diary = diary
            sidenote.author = request.user
            sidenote.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                sidenotes_html = render_to_string('sidenotes_list.html', {'sidenotes': sidenotes})
                return JsonResponse({'sidenotes_html': sidenotes_html})
        return render(request, 'diary_detail.html', {'diary': diary})
    else:
        form = SidenoteForm()
    return render(request, 'diary_detail.html', {'diary': diary, 'sidenotes': sidenotes, 'form': form})
    



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