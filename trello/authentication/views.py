from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт был создан, теперь вы можете зайти в него!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, '../templates/registration/register.html', {'form': form})