from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    word = get_random_string(length=9,allowed_chars='abcdefghijklmnopqrstuvwxyz')
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    context = {
    'word': word
    }
    return render(request, 'index.html', context)

def generate_random_word(request):
    return redirect('/random_word')

def clear(request):
    request.session['count'] = 0
    return redirect('/random_word')
