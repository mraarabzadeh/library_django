from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from library.Forms import SignUpForm, AddBookForm, NewSignUpForm, SearchBookForm
from library.models import Book


def SignUp(request):
    if request.method == 'POST':
        form = NewSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('base'))
    else:
        form = NewSignUpForm()
    return render(request, 'signup.html', {'form': form})


class SignUpClass(FormView):
    template_name = 'signup.html'
    form_class = NewSignUpForm
    success_url = reverse_lazy('base')


def HomePage(request):
    data = Book.AllBook.all()
    page = Paginator(data, 1)
    page_number = request.GET.get('page')
    form = page.get_page(page_number)
    return render(request, 'HomePage.html', {'form': form})


def AddBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('base'))
    else:
        form = AddBookForm()
    return render(request, 'AddBook.html', {'form':form})


def SearchBook(request):
    if request.POST:
        title = SearchBookForm(request.POST)
        title.is_valid()
        title = title.cleaned_data['title']
        result = Book.AllBook.filter(title__contains=title)
        return render(request, 'ShowBookSearchResult.html', {'result': result})

    return render(request, 'SearchBooks.html', {'form':SearchBookForm()})