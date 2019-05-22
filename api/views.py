import json
from datetime import datetime
from calendar import monthrange
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import UsersSerializer, Users, Shifts, ShiftsSerializer


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
        new_user = Users.objects.create(email=val['email'], phone_number=val['phone_number'], f_name=val['f_name'], l_name=val['l_name'], role=val['role'])
        new_user.save()
        return Response('datos guardados', status=status.HTTP_200_OK)

    def delete(self, request, id):

        users = Users.objects.get(id=id)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):

        users = Users.objects.get(id=id)
        val = json.loads(request.body)
        users.email= val['email']
        users.phone_number= val['phone_number']
        users.f_name= val['f_name']
        users.l_name= val['l_name']
        users.role= val['role']
        users.save()
        return Response('ok', status=status.HTTP_200_OK)


class ShiftViews (APIView):

    def get (self, request, date=None):

        mrange = monthrange(int(date[:4]), int(date[5:7]))
        lastday = str(mrange[1])
        datesum = date+"-01"
        datestart = datetime.strptime(datesum, "%Y-%m-%d")
        dateend = datetime.strptime(str(date+"-"+lastday), "%Y-%m-%d")
        shifts = Shifts.objects.filter(date_start__lte = dateend, date_end__gte = datestart)
        serializer = ShiftsSerializer(shifts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
