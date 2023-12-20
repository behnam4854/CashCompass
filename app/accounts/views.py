from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BudegtForm
# Create your views here.

def home(request):
    form = BudegtForm()
    if request.method == 'post':
        form = BudegtForm(request.post)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
        else:
            form = BudegtForm()
    return render(request,'home.html', {"form": form})