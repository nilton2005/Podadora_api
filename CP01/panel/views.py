# views.py
from argparse import Action
from rest_framework import viewsets
from .models import Mower, Command, SensorData, Route
from .serializer import MowerSerializer, CommandSerializer, SensorDataSerializer, RouteSerializer

class MowerViewSet(viewsets.ModelViewSet):
    queryset = Mower.objects.all()
    serializer_class = MowerSerializer

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class MowerViewSet(viewsets.ModelViewSet):
    queryset = Mower.objects.all()
    serializer_class = MowerSerializer
    
    @Action(detail=True, methods=['patch'])
    def update_mower_data(self, request, pk=None):
        # Extrae y valida los datos de recorrido y tiempo de encendido
        recorrido = request.data.get('recorrido')
        tiempo_encendido = request.data.get('tiempo_encendido')
        
        # Actualiza el modelo con los nuevos valores
        mower = self.get_object()
        mower.recorrido = recorrido
        mower.tiempo_encendido = tiempo_encendido
        mower.save()
        
        return Response({'status': 'Datos actualizados'}, status=status.HTTP_200_OK)

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    
    @Action(detail=True, methods=['patch'])
    def update_command_data(self, request, pk=None):
        # Extrae y valida los datos del comando
        nuevo_comando = request.data.get('comando')
        
        # Actualiza el modelo con los nuevos valores
        command = self.get_object()
        command.comando = nuevo_comando
        command.save()
        
        return Response({'status': 'Comando actualizado'}, status=status.HTTP_200_OK)

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

    @Action(detail=True, methods=['patch'])
    def update_sensor_data(self, request, pk=None):
        # Extrae los datos específicos de los sensores
        temperatura = request.data.get('temperatura')
        humedad = request.data.get('humedad')
        
        # Actualiza el modelo de datos de sensores
        sensor_data = self.get_object()
        sensor_data.temperatura = temperatura
        sensor_data.humedad = humedad
        sensor_data.save()
        
        return Response({'status': 'Datos del sensor actualizados'}, status=status.HTTP_200_OK)
    

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    @Action(detail=True, methods=['patch'])
    def update_route_data(self, request, pk=None):
        # Extrae los datos específicos de la ruta
        nueva_ruta = request.data.get('ruta')
        
        # Actualiza el modelo de datos de ruta
        route = self.get_object()
        route.ruta = nueva_ruta
        route.save()
        
        return Response({'status': 'Ruta actualizada'}, status=status.HTTP_200_OK)


