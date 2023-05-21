from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from .models import Animal, Adoption


def adoption_summary(request):
    return render(request, 'adoption_page.html')


def all_pets_alba(request):
    pets = Animal.objects.all()
    return render(request, 'alba.html', {'pet': pets})


def all_pets_sibiu(request):
    pets = Animal.objects.all()
    return render(request, 'sibiu.html', {'pet': pets})


def all_pets_cluj(request):
    pets = Animal.objects.all()
    return render(request, 'cluj.html', {'pet': pets})


def animal_detail(request, slug):
    pets = get_object_or_404(Animal, slug=slug, available=True)
    return render(request, 'detail_animal.html', {'pet': pets})


def formular(request):
    return render(request, 'formular.html')


def add(request):
    if request.method == 'POST':
        nume = request.POST.get('nume', '')
        prenume = request.POST.get('prenume', '')
        adresa = request.POST.get('adresa', '')
        oras = request.POST.get('oras', '')
        telefon = request.POST.get('telefon', '')
        email = request.POST.get('email', '')
        adapost = request.POST.get('adapost', '')
        user = request.user.username

        adoption = Adoption(user=user, nume=nume, prenume=prenume, adresa=adresa, oras=oras, telefon=telefon, email=email, adapost=adapost)
        adoption.save()

        subject = 'Adoption request received'
        message = f'Hello {nume} {prenume},\n\nThank you for submitting your adoption request. We have received your request and will process it shortly.\n\nBest regards,\nThe Pet Shop and Pet Rescue Center team'
        from_email = 'herleadenisa12@yahoo.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

    return render(request, 'succes_adopt.html')
