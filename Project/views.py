from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User


class Main(APIView):
    # def get(self, request):
    #     user_list = User.objects.all().order_by('-id')
    #     return render(request, 'project/main.html', context=dict(user_list=user_list))


    # def get(self, request):
    #     user_list = User.objects.all()
    #     return render(request, 'project/sample.html', context=dict(user_list=user_list))

    # def get(self, request):
    #     user_list = User.objects.all()
    #     return render(request, 'project/detail.html', context=dict(user_list=user_list))

    def get(self, request):
        user_list = User.objects.all().order_by('-id')
        return render(request, 'project/sample.html', context=dict(user_list=user_list))

# class AddUser(APIView):
#     def post(self, request):
#
#         name = request.data.get('name')
#         car_num = request.data.get('car_num')
#
#         print(name)
#         print(car_num)
#
#         return Response(status=200)

