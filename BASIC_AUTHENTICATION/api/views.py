from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated,AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message":"This is Public View"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({"message":"This is private View"})