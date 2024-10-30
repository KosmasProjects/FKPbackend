from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Organization
from .serializers import OrganizationSerializer

@api_view(["GET"])
def organization_list(request):
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)