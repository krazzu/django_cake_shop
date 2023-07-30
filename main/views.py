from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/main.html', data)
