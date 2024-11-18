from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import logout, login

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("shop:index")
        else:
            return render(request, 'registration/registration.html', {'form': form})

    else:
        form = UserRegistrationForm()

        return render(request, 'registration/registration.html', {'form': form})


def logout_user(request):
    logout(request)

    return redirect('shop:index')