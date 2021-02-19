from django.shortcuts import render


def index(request):
    host = request.get_host()
    context = {'host': host}
    return render(request, 'index.html', context)
