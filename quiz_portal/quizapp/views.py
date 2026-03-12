from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Question, Result
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists. Please choose another username.")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request,)
        return redirect('login')

    return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html')




def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def quiz_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for q in questions:
            if request.POST.get(str(q.id)) == q.correct_answer:
                score += 1
        Result.objects.create(user=request.user, score=score)
        return redirect('result')
    return render(request, 'quiz.html', {'questions': questions})


@login_required
def result_view(request):
    result = Result.objects.filter(user=request.user).last()
    return render(request, 'result.html', {'result': result})