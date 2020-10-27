from rest_framework import viewsets

from ..models import Sample
from .serializers import SampleListSerializer, SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_action_classes = {
            "list": SampleListSerializer,
            "create": SampleSerializer,
            "retrieve": SampleSerializer,
            "update": SampleSerializer,
            "partial_update": SampleSerializer,
            "destroy": SampleSerializer,
        }

    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        kwargs["partial"] = True
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
