from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import UserForm


date = datetime.datetime.now()
test_list = [i for i in range(1, 10)]
context = {"test_list": test_list,
            "date" : datetime.datetime.now()}
def index(request):
    # Here  i show, that we can send data to a template, i am sending a list.
    return render(request, "First_App/index.html", context)

def test_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect('index') # The name of the view or url pattern needs to be given
    else:
        form = UserForm()
    return render(request, "First_App/test_form.html", {"form" : form})
