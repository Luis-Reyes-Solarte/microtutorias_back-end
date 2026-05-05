from rest_framework.viewsets import ModelViewSet

from .models import TutoringAd
from .serializers import TutoringAdSerializer


class TutoringViewSet(ModelViewSet):
    queryset = TutoringAd.objects.all()
    serializer_class = TutoringAdSerializer
