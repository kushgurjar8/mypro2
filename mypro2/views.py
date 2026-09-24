from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    total = None
    if request.method == 'POST' and 'num1' in request.POST:
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        total = num1 + num2
    return render(request, 'result.html', {'total': total})

def index(request):
    return render(request, 'index.html')