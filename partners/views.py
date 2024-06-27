from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Partner
from .serializers import PartnerSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def partner_list(request):
    partners = Partner.objects.all()
    serializer = PartnerSerializer(partners, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)