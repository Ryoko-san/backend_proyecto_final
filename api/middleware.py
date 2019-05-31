from django.urls import reverse 
from rest_framework import status
from django.http import HttpResponse

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path_admin = ["/api/users/<int:id>", '/api/shifts/<int:id>', '/api/shifts-types/<int:id>', 
                        '/api/positions/<int:id>', "/api/users/"]
        print(path_admin)
        print(request.user.is_authenticated)
        print(request.path)
        if request.user.is_authenticated:
            print("entro al primer if")
            if request.path in path_admin and request.user.is_staff:
                print("entro al segundo")
                response = self.get_response(request)
                return response
            elif request.path in path_admin and request.user.is_staff == False:
                print("No está autorizado (elif)")
                return HttpResponse("Usuario no autorizado")
            else:
                print("else")
                response = self.get_response(request)
                return response
        if request.path == "/login/" or request.path == "/api/login/":
            response = self.get_response(request)
            return response
        else: 
            print("No está autenticado (no entro a ningun if)")
            return HttpResponse("No hay un usuario autenticado")
        