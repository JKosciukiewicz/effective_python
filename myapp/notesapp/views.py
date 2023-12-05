from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Note

# Create your views here.
def home(request):
    context={
        'notes': Note.objects.all()
    }
    return render(request, 'notesapp/home.html',context)
