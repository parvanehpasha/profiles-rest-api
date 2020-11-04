from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'User Http get push create and delete',
            'hello word',
            'i learning django',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

