"""
author: Varun
"""

# from rest_framework.views import APIView
# from rest_framework import status

from django.views import View
from django.http import HttpResponse


class Home(View):
    """Landing Page"""

    def get(self, request):
        """returns home page"""
        return HttpResponse('Hey')
