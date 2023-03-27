from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Exhibit, Event, Talent, Review, Favorite
from .forms import ExhibitForm, EventForm, TalentForm, ReviewForm


def home(request):
    exhibits = Exhibit.objects.all()
    events = Event.objects.all()
    talents = Talent.objects.all()
    return render(request, 'home.html', {'exhibits': exhibits, 'events': events, 'talents': talents})


@login_required
def create_exhibit(request):
    if request.method == 'POST':
        form = ExhibitForm(request.POST)
        if form.is_valid():
            exhibit = form.save(commit=False)
            exhibit.save()
            messages.success(request, 'Exhibit created successfully!')
            return redirect('home')
    else:
        form = ExhibitForm()
    return render(request, 'create_exhibit.html', {'form': form})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def create_talent(request):
    if request.method == 'POST':
        form = TalentForm(request.POST)
        if form.is_valid():
            talent = form.save(commit=False)
            talent.save()
            messages.success(request, 'Talent created successfully!')
            return redirect('home')
    else:
        form = TalentForm()
    return render(request, 'create_talent.html', {'form': form})


@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Review created successfully!')
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})


@login_required
def create_favorite(request, id, type):
    if type == 'exhibit':
        obj = Exhibit.objects.get(pk=id)
    elif type == 'event':
        obj = Event.objects.get(pk=id)
    elif type == 'talent':
        obj = Talent.objects.get(pk=id)
    else:
        messages.error(request, 'Invalid favorite type!')
        return redirect('home')
    favorite, created = Favorite.objects.get_or_create(
        user=request.user, **{type: obj})
    if created:
        messages.success(request, f'{obj.title} added to favorites!')
    else:
        favorite.delete()
        messages.success(request, f'{obj.title} removed from favorites!')
    return redirect('home')




@login_required
def delete_review(request, id):
    review = Review.objects.get(pk=id)
    if review.user != request.user:
        messages.error(request,id)
