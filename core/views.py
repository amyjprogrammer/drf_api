from django.shortcuts import render

#third-party imports
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "name": 'john',
            'age': 23,
        }

        return Response(data)

