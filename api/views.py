import json
from datetime import datetime
from calendar import monthrange
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import UsersSerializer, Users, Positions, Shifts, ShiftsSerializer

"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


class UsersView(APIView):

    def get(self, request):

        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):

        val = json.loads(request.body)
        new_user = Users.objects.create_user(val['first_name'] + "_" + val['last_name'], val['email'], val['first_name'][0] + val['last_name'])
        new_user.first_name = val['first_name']
        new_user.last_name = val['last_name']
        new_user.phone_number = val['phone_number']
        positions_id = Positions.objects.get(id=val["positions_id"])
        new_user.positions_id = positions_id
        new_user.save()
        return Response(val, status=status.HTTP_200_OK)

    def delete(self, request, id):

        users = Users.objects.get(id=id)
        users.is_active = False
        users.save()
        return Response('ok', status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):

        users = Users.objects.get(id=id)
        val = json.loads(request.body)
        users.email= val['email']
        users.phone_number= val['phone_number']
        users.first_name= val['first_name']
        users.last_name= val['last_name']
        positions_id = Positions.objects.get(id=val["positions_id"])
        users.positions_id= positions_id
        users.save()
        return Response('ok', status=status.HTTP_200_OK)


class ShiftViews (APIView):

    def get (self, request, date=None):
        if request.user.id is not None:
            id = request.user.id
        mrange = monthrange(int(date[:4]), int(date[5:7]))
        lastday = str(mrange[1])
        datesum = date+"-01"
        datestart = datetime.strptime(datesum, "%Y-%m-%d")
        dateend = datetime.strptime(str(date+"-"+lastday), "%Y-%m-%d")
        if id is not None:
            shifts = Shifts.objects.filter(date_start__lte = dateend, date_end__gte = datestart, users_id=id)
            serializer = ShiftsSerializer(shifts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            shifts = Shifts.objects.filter(date_start__lte = dateend, date_end__gte = datestart)
            serializer = ShiftsSerializer(shifts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) 

