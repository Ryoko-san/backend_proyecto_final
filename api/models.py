"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models
import datetime


class Users(models.Model):
    __tablename__ = 'Users'
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=False)
    f_name = models.CharField(max_length=250, null=False)
    l_name = models.CharField(max_length=250, null=False)
    role = models.CharField(max_length=250, null=False)
    positions_id = models.ForeignKey('Positions', on_delete=models.CASCADE)

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'phone_number', 'f_name', 'l_name', 'role')


class Shifts(models.Model):
    __tablename__ = 'Shift'
    task = models.CharField(max_length=250, null=False)
    date = datetime.date.today()
    users_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    shift_types_id = models.ForeignKey('Shift_types', on_delete=models.CASCADE)


class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = ('task', 'date')


class Positions(models.Model):
    __tablename__ = 'Positions'
    position_name = models.CharField(max_length=250, null=False)


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ('position_name')


class Shift_types(models.Model):
    __tablename__ = 'Shift_types'
    shift_name = models.CharField(max_length=250, null=False)
    shift_start = models.DateField(max_length=250, null=False)
    shift_end = models.DateField(max_length=250, null=False)


class Shift_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift_types
        fields = ('shift_name', 'shift_start', 'shift_end')


class Client(models.Model):
    __tablename__ = 'Client'
    client_name = models.CharField(max_length=250, null=False)
    users_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    shifts_id = models.ForeignKey('Shifts', on_delete=models.CASCADE)


class ClienttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_name')
