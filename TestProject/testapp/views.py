from django.shortcuts import render, HttpResponse

global_var = "hello world"

def index(request):
    return HttpResponse('<h1>Hello From Views.py</h1>')

def test(request):
    return render(request, 'testhtml.html', {'variable': global_var})


def test2(request):
    return render(request, 'test2.html')