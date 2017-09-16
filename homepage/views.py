from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/homepage.html')

def rejestr_zolnierzy(request):
    return render(request, 'homepage/rejestr.html')


