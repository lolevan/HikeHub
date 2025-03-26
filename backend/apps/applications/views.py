from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationCreateSerializer
from .tasks import create_application_task


class ApplicationCreateView(APIView):
    """Принимает данные заявки и инициирует асинхронное создание."""
    def post(self, request, hike_id):
        serializer = ApplicationCreateSerializer(data=request.data)
        if serializer.is_valid():
            create_application_task.delay(
                hike_id,
                serializer.validated_data['name'],
                serializer.validated_data['email'],
                serializer.validated_data['phone']
            )
            return Response({'detail': 'Application is being processed'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
