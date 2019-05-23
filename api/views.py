import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import UsersSerializer, Users, Positions


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
        new_user = Users.objects.create(email=val['email'], phone_number=val['phone_number'], f_name=val['f_name'], l_name=val['l_name'], role=val['role'], positions_id=positions_id)
        new_user.save()
        return Response(json.dumps(val), status=status.HTTP_200_OK)

    def delete(self, request, id):

        users = Users.objects.get(id=id)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):

        users = Users.objects.get(id=id)
        #users_list = request.data["list"]
        #for task in users_list:
            #new_user = Users.objects.all()
            #new_user.save()
        #new_user = Users.objects.all()
        val = json.loads(request.body)
        users.email= val['email']
        users.phone_number= val['phone_number']
        users.f_name= val['f_name']
        users.l_name= val['l_name']
        users.role= val['role']
        users.save()
        #serializer = UsersSerializer(users, many=True)
        return Response(json.dumps('ok'), status=status.HTTP_200_OK)