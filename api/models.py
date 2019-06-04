import datetime
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    __tablename__ = 'Users'
    phone_number = models.CharField(max_length=150, null=False)
    positions_id = models.ForeignKey('Positions', on_delete=models.CASCADE, null=True)

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'positions_id', 'is_active')


class Shifts(models.Model):
    __tablename__ = 'Shift'
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    users_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    shift_types_id = models.ForeignKey('Shift_types', on_delete=models.CASCADE)
    task = models.CharField(max_length=250, null=True)


class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = ('date_start', 'date_end', 'users_id', 'shift_types_id', 'task', 'id')


class Positions(models.Model):
    __tablename__ = 'Positions'
    position_name = models.CharField(max_length=250, null=False)


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ('position_name', 'id')


class Shift_types(models.Model):
    __tablename__ = 'Shift_types'
    shift_name = models.CharField(max_length=250, null=False)
    shift_start = models.TimeField()
    shift_end = models.TimeField()


class Shift_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift_types
        fields = ('shift_name', 'shift_start', 'shift_end', 'id')


class Client(models.Model):
    __tablename__ = 'Client'
    client_name = models.CharField(max_length=250, null=False)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_name')
