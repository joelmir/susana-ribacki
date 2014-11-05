from django.shortcuts import render
import json

from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
  # return render(request, 'core/em_breve.html')
  return render(request, 'core/index.html')

def contact(request):
  message = request.POST.get('message')
  phone = request.POST.get('phone')
  message = request.POST.get('message')
  name = request.POST.get('name')
  email = request.POST.get('email')

  content = '''
  Nome: {name}
  Telefone: {phone}
  Email: {email}
  Mensagem: {message}
  '''.format(name=name, phone=phone, email=email, message=message)
  
  send_mail('Contato Site',content, settings.DEFAULT_FROM_EMAIL,
    settings.SERVER_EMAIL, fail_silently=False)

  return HttpResponse(json.dumps('Email Enviado com sucesso'), content_type="application/json")
