from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Ticket
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .Serializers import TicketSerializer

class CrearTicket(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        ticket = Ticket.objects.create(
            titulo =request.data['titulo'],
            descripcion=request.data['descripcion'],
            numero_equipo=request.data['numero_equipo'],
            usuario=request.user
        )
        return Response({"msg": "Ticket creado"}, status=201)
    
class ListarTickets(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        estado = request.query_params.get('estado')

        if request.user.rol == 'tecnico':
            tickets = Ticket.objects.all()
        else:
            tickets = Ticket.objects.filter(usuario=request.user)

        if estado:
            tickets = tickets.filter(estado=estado)

        data = TicketSerializer(tickets, many=True).data
        return Response(data)
    
class ActualizarTicket(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):

            if request.user.rol != 'tecnico':
                return Response(
                    {"error": "No autorizado"},
                    status=403
                )

            try:
                ticket = Ticket.objects.get(id=id)
            except Ticket.DoesNotExist:
                return Response(
                    {"error": "Ticket no encontrado"},
                    status=404
                )

        
            nuevo_estado = request.data.get('estado')

            estados_validos = ['pendiente', 'en_revision', 'resuelto']
            if nuevo_estado not in estados_validos:
                return Response(
                    {"error": "Estado inválido"},
                    status=400
                )


            ticket.estado = nuevo_estado

            if nuevo_estado == 'resuelto':
                ticket.fecha_resolucion = timezone.now()

            ticket.save()

        
            channel_layer = get_channel_layer()

            async_to_sync(channel_layer.group_send)(
                "alertas",
                {
                    "type": "enviar_alerta",
                    "message": {
                        "mensaje": f"El ticket #{ticket.id} ahora está en estado {ticket.estado}"
                    }
                }
            )

        
            return Response(
                {
                    "msg": "Ticket actualizado correctamente",
                    "ticket_id": ticket.id,
                    "nuevo_estado": ticket.estado
                },
                status=200
            )
        
class Estadisticas(APIView):
    def get(self, request):
        total = Ticket.objects.count()
        pendientes = Ticket.objects.filter(estado='pendiente').count()
        resueltos = Ticket.objects.filter(estado='resuelto').count()

        return Response({
            "total": total,
            "pendientes": pendientes,
            "resueltos": resueltos
        })
    