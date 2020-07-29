from rest_framework import viewsets

from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @action(detail=False, methods=['get'])
    def lol(self, request, pk=None):
        return Response({'status': 'OK'})
