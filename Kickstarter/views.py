from django.http import HttpResponse
from django.shortcuts import render


def handler404(request, exception):
    print("404 handler called!")  # Debug print
    return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    print("500 handler called!")
    return render(request, '500.html', status=500)


def handler403(request, exception):
    print("403 handler called!")
    return render(request, '403.html', status=403)
