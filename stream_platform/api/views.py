from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status

from ..models import StreamPlatform
from .serializers import StreamPlatformSerializer


class StreamPlatformListAV(APIView):
    def get(self, request: Request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms,
                                              many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = StreamPlatformSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


class StreamPlatformDetailAV(APIView):
    def get(self, request: Request, platform_pk: int):
        platform = StreamPlatform.objects.get(id=platform_pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request: Request, platform_pk: int):
        platform = StreamPlatform.objects.get(id=platform_pk)
        serializer = StreamPlatformSerializer(platform,
                                              data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, platform_pk: int):
        platform = StreamPlatform.objects.get(id=platform_pk)
        platform.delete()
        return Response(status=status.HTTP_200_OK)
