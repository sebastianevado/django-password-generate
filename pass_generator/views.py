from django.shortcuts import render
# from django.http import HttpResponse
import random
# Create your views here.
def about(request):
    return render(request, 'pass_generator/about.html')

def home(request):
    return render(request, 'pass_generator/home.html')

def password(request):

    lenght = int(request.GET.get('lenght'))
    characters = list('abcdebcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEBCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){}|'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))    
    for x in range(lenght):
        generated_password += random.choice(characters)
    return render(request, 'pass_generator/password.html', {'password': generated_password})
