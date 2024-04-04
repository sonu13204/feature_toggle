from rest_framework import generics
from .models import FeatureToggle
from .serializers import FeatureToggleSerializer


class FeatureToggleListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeatureToggle.objects.all()
    serializer_class = FeatureToggleSerializer


class FeatureToggleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeatureToggle.objects.all()
    serializer_class = FeatureToggleSerializer
