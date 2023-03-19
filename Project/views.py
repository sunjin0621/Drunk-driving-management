from django.shortcuts import render
from rest_framework.views import APIView

from user.models import User


class Main(APIView):
    def get(self, request):
        user_list = User.objects.all()
        return render(request, 'project/main.html', context=dict(user_list=user_list))

