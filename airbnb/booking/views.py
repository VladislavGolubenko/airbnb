from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import FormFindHotel, FormAddHotel


def index(request):
    booking = Booking.objects.all()
    context = {'booking': booking}
    return render(request, template_name='booking/index.html', context=context)


def realty(request):
    booking = Booking.objects.all()
    realty = Realty.objects.all()
    pictures = Pictures.objects.all()
    if request.method == 'POST':
        form = FormFindHotel(request.POST)
        if form.is_valid() and form.is_bound:
            graid = form.cleaned_data['graid']
            region = form.cleaned_data['region']
            from_date = form.cleaned_data['from_date']
            peoples = form.cleaned_data['peoples']
            if graid and region and from_date and peoples:
                Realty.objects.filter(region=region, rating=graid, bedrooms=peoples, )

    else:
        form = FormFindHotel
    context = {'booking': booking, 'form': form, 'realty': realty, 'img': pictures}
    return render(request, template_name='booking/jobs.html', context=context)


def get_booking(request, id_realty_id):
    booking = Booking.objects.filter(id_realty_id=id_realty_id)
    realties = Booking.objects.all()
    pictures = Pictures.objects.all()
    realty = Booking.objects.get(pk=id_realty_id)
    return render(request, 'booking/job_details.html',
                  {'booking': booking, 'realties': realties, 'realty': realty, 'images': pictures})


def add_realty(request):
    if request.method == 'POST':
        form = FormAddHotel(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            realty = Realty.objects.create(**form.cleaned_data)
            return redirect(realty)
    else:
        form = FormAddHotel()
    return render(request, 'booking/add_hotel.html', {'form': form})
