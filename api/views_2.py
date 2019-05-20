import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Users, Shifts, ShiftsSerializer, Shift_types, Shift_typesSerializer
from datetime import datetime

class ShiftsView(APIView):
    def get(self, request, date=None):
        if date is None:
            shifts = Shifts.objects.all()
            serializer = ShiftsSerializer(shifts,  many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            date_filter = datetime.strptime(date, "%Y-%m-%d")
            shifts = Shifts.objects.filter(date_start__lte = date_filter, date_end__gte = date_filter)
            serializer = ShiftsSerializer(shifts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        newShift = json.loads(request.body)
        shift_types_id = Shift_types.objects.get(id=newShift["shift_types_id"])
        users_id = Users.objects.get(id=newShift["users_id"])
        Shifts.objects.create(date_start=newShift["date_start"],date_end=newShift["date_end"], users_id=users_id, shift_types_id=shift_types_id, task=newShift["task"])
        return Response("Nuevo turno creado", status=status.HTTP_200_OK)

    def delete(self, request, id):
        shift = Shifts.objects.filter(id = id)
        shift.delete()
        return Response("Turno eliminado", status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        shift = json.loads(request.body)
        shift_types_id = Shift_types.objects.get(id=shift["shift_types_id"])
        users_id = Users.objects.get(id=shift["users_id"])
        new = Shifts(id=id, date_start=shift["date_start"],date_end=shift["date_end"], users_id=users_id, shift_types_id=shift_types_id, task=shift["task"])
        new.save()
        return Response("Turno actualizado", status=status.HTTP_200_OK)


class ShiftTypesView(APIView):
    def get(self, request):
        s_type = Shift_types.objects.all()
        serializer = Shift_typesSerializer(s_type,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        new_type = json.loads(request.body)
        Shift_types.objects.create(shift_name=new_type["shift_name"], shift_start=new_type["shift_start"], shift_end=new_type["shift_end"])
        return Response("Nuevo tipo de turno creado", status=status.HTTP_200_OK)