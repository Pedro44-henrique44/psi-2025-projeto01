from django.shortcuts import render

def index(request):
    return render(request, "MeuSite/index.html")

def elenco(request):
    return render(request, "MeuSite/elenco.html")

def sobre(request):
    return render(request, "MeuSite/sobre.html")
# Create your views here.
