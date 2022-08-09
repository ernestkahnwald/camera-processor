from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.request import Request

from .utils import process_image


class ProcessImageView(APIView):
    def post(self, request: Request, *args, **kwargs):
        image = process_image(request.data['image'])
        return HttpResponse(image, content_type='image/png')
