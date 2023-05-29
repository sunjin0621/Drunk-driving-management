import os
from uuid import uuid4
from rest_framework.response import Response
from rest_framework.views import APIView
from Project.settings import MEDIA_ROOT
from user.models import User


class AddUser(APIView):
    def post(self, request):

        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)


        name = request.data.get('name')
        car_num = request.data.get('car_num')
        phone_num = request.data.get('phone_num')

        User.objects.create(name='name', car_num='car_num', phone_num='phone_num')

        print(name)
        print(car_num)
        print(phone_num)

        return Response(status=200)
