from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
# Create your views here.
