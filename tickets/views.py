from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Flight,Booking

def flight_list(request):
    flights = Flight.objects.all()
    return render(request,'flight_list.html',{'flights':Flight})

@login_required
def book_flight(request,flight_id):
    flight = Flight.objects.get(pk=flight_id)

    if request.method == 'POST':
        Booking.objects.create(user=request.user,flight=Flight)
        return redirect('flight_list')
    return render(request,'book_flight.html',{'flight': flight})


