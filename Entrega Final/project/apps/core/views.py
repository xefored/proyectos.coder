from django.shortcuts import redirect, render

from . import models

from . import forms

from django.contrib.auth.views import LoginView


def index(request):
    return render(request, "core/index.html")


def Hoteles_list(request):
    consulta = models.Hoteles.objects.all()
    contexto = {"hoteles": consulta}
    return render(request, "core/Hoteles_list.html", contexto)

def Hoteles_form(request):
    if request.method == "POST":
        form = forms.HotelesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Hoteles_list")
    else:
        form = forms.HotelesForm()
    return render(request, "core/Hoteles_form.html", {"form" : form})





def Destinos_list(request):
    consulta = models.Destinos.objects.all()
    contexto = {"destinos": consulta}
    return render(request, "core/Destinos_list.html", contexto)

def Destinos_form(request):
    if request.method == "POST":
        form = forms.DestinosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Destinos_list")
    else:
        form = forms.DestinosForm()
    return render(request, "core/Destinos_form.html", {"form" : form})



class CustomLoginView(LoginView):
    authentication_form = forms.CustonAuthenticationForm
    template_name = "core/login.html"