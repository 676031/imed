from django.shortcuts import render
import requests

def button(request):
    return render(request, 'home.html')

def external(request):
    inp=request.POST.get('keyword')
    out= run([sys.executable, 'telegram-sender.py' ,inp],shell=False, stdout=PIPE)
    print(out)
    return render(request, 'home.html',{'data':data})