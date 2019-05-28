import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import UsersSerializer, Users, Positions
from django.contrib.auth.models import User


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
        positions_id = Positions.objects.get(id=val["positions_id"])
        user_id = User.objects.get(id=val["user_id"])
        new_user = Users.objects.create(email=val['email'], phone_number=val['phone_number'], f_name=val['f_name'], l_name=val['l_name'], user_id=user_id, positions_id=positions_id)
        new_user.save()
        return Response(val, status=status.HTTP_200_OK)

    def delete(self, request, id):

        users = Users.objects.get(id=id)
        users.delete()
        return Response('ok', status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):

        users = Users.objects.get(id=id)
        val = json.loads(request.body)
        users.email= val['email']
        users.phone_number= val['phone_number']
        users.f_name= val['f_name']
        users.l_name= val['l_name']
        user_id = User.objects.get(id=val["user_id"])
        users.user_id = user_id
        positions_id = Positions.objects.get(id=val["positions_id"])
        users.positions_id= positions_id
        users.save()
        return Response('ok', status=status.HTTP_200_OK)