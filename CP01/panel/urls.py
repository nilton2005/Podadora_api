# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para MowerViewSet
    path('api/mowers/', views.MowerViewSet.as_view({'get': 'list', 'post': 'create'}), name='mower-list-create'),
    path('api/mowers/<int:pk>/', views.MowerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='mower-detail'),

    # Rutas para CommandViewSet
    path('api/commands/', views.CommandViewSet.as_view({'get': 'list', 'post': 'create'}), name='command-list-create'),
    path('api/commands/<int:pk>/', views.CommandViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='command-detail'),

    # Rutas para SensorDataViewSet
    path('api/sensor-data/', views.SensorDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='sensor-data-list-create'),
    path('api/sensor-data/<int:pk>/', views.SensorDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='sensor-data-detail'),

    # Rutas para RouteViewSet
    path('api/routes/', views.RouteViewSet.as_view({'get': 'list', 'post': 'create'}), name='route-list-create'),
    path('api/routes/<int:pk>/', views.RouteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='route-detail'),
]
