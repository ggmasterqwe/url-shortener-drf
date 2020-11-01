from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UrlPostSerializer
# Create your views here.

class UrlCreateApi(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UrlPostSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().post(request, *args, **kwargs)