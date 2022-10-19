from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.


def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    context = {'contact': 'active'}

    if request.method == 'POST':
        contct = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contct.name = name
        contct.email = email
        contct.message = message
        contct.subject=subject
        contct.save()
        messages.success(request, 'Contact request submitted successfully.')

    return render(request, 'core/conact.html', context)
