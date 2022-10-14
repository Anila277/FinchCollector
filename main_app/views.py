from curses.ascii import CR
from distutils.log import error
import imp
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect 
from .models import Finch, StuffWithFinch
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)
    return render(request, 'finches/index.html', {'finches': finches})

@login_required
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    stuffs = StuffWithFinch.objects.exclude(id__in=finch.stuffs.all().values_list('id'))
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form, 'stuffs': stuffs
        })
@login_required
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches_detail', finch_id=finch_id)

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('finches_index')
        else:
            error_message = 'Signup input invalid'
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context )

def assoc_stuff(request, finch_id, stuff_id):
    Finch.objects.get(id=finch_id).stuffs.add(stuff_id)
    return redirect('finches_detail', finch_id=finch_id)

class FinchesCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = ('name', 'type', 'colors')

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)

class FinchesUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = ('type', 'colors')

class FinchesDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url = '/finches/'

class StuffWithFinchIndex(LoginRequiredMixin, ListView):
    model = StuffWithFinch

class StuffWithFinchCreate(LoginRequiredMixin, CreateView):
    model = StuffWithFinch
    fields = '__all__'

class StuffWithFinchDetail(LoginRequiredMixin, DetailView):
    model = StuffWithFinch

class StuffWithFinchDelete(LoginRequiredMixin, DeleteView):
    model = StuffWithFinch
    success_url = '/stuffs/'

class StuffWithFinchUpDate(LoginRequiredMixin, UpdateView):
    model = StuffWithFinch
    fields = '__all__'

