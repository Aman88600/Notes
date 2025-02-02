from django.shortcuts import render
from django.http import HttpResponse
import datetime

date = datetime.datetime.now()
test_list = [i for i in range(1, 10)]
context = {"test_list": test_list,
            "date" : datetime.datetime.now()}
def index(request):
    # Here  i show, that we can send data to a template, i am sending a list.
    return render(request, "First_App/index.html", context)
