import os
from uuid import uuid4

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from Project.settings import MEDIA_ROOT
from user.models import User


class Main(APIView):
    def get(self, request):
        user_list = User.objects.all().order_by('-id')
        return render(request, 'project/sample.html', context=dict(user_list=user_list))

class UploadUser(APIView):
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        name = request.data.get('name')
        phone_num = request.data.get('phone_num')
        car_num = request.data.get('car_num')
        address = request.data.get('address')

        print(file)
        print(image)
        print(name)
        print(phone_num)
        print(car_num)
        print(address)


        User.objects.create(image=image, name=name, car_num=car_num, phone_num=phone_num, address=address)

        return Response(status=200)

def main(request):
    userlist = User.objects.all()

    return render(request, 'project/sample.html', {'userlist':userlist})


def detail(request, id):
    user_detail = get_object_or_404(User, pk=id)
    return render(request, 'project/detail.html', {'user': user_detail})







