from rest_framework import generics

from .models import TutoringAd
from .serializers import TutoringAdSerializer


# Create your views here.
class TutoringListView(generics.ListAPIView):
    queryset = TutoringAd.objects.all()
    serializer_class = TutoringAdSerializer
