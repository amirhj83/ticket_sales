from django.urls import path
from .views import flight_list,book_flight

urlpatterns = [
    path('flights/',flight_list,name='flight_list'),
    path('book/<int:flight_id>/',book_flight,name='book-flight'),
]