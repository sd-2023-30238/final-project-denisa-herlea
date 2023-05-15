from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render

from basket.basket import Basket
from .models import Order


def add(request):
    if request.method == 'POST':
        nume = request.POST.get('nume', '')
        prenume = request.POST.get('prenume', '')
        adresa = request.POST.get('adresa', '')
        oras = request.POST.get('oras', '')
        zip = request.POST.get('zip', '')

        basket = Basket(request)
        baskettotal = basket.get_total_price()

        order = Order(nume=nume, prenume=prenume, adresa=adresa, oras=oras, cod_postal=zip, total_paid=baskettotal)
        order.save()
    return render(request, 'succes.html')
