# serializers.py
from rest_framework import serializers
from .models import Mower, Command, SensorData, Route

class MowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mower
        fields = ['id', 'name', 'status', 'battery_level', 'last_update']

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'mower', 'command_type', 'timestamp']

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'mower', 'obstacle_detected', 'timestamp']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'mower', 'position_x', 'position_y', 'timestamp']
