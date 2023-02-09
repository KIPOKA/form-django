from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
    form = ContactForm()
    return render(request, 'form.html', {'form': form})


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            form.save()
    form = ContactForm()
    return render(request, 'form.html', {'form': form})
