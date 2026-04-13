from django.urls import path 
from .views import CrearTicket,ListarTickets,ActualizarTicket,Estadisticas

urlpatterns = [
    path('tickets/', CrearTicket.as_view(), name = 'tickets'),
    path('tickets/list/', ListarTickets.as_view() , name = 'Listar_tickets'),
    path('tickets/<int:id>/', ActualizarTicket.as_view(), name='Actualizar_tickets'),
    path('tickets/estadisticas/', Estadisticas.as_view(), name = ' Estadisticas') ,

]