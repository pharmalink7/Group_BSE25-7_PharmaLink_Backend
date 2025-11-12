# apps/pharmacies/views.py

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
# We don't need these for the secure version
# from rest_framework.exceptions import ValidationError
# from django.contrib.auth import get_user_model
from .models import Pharmacy, Medicine
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import PharmacySerializer, MedicineSerializer
from django.shortcuts import render
from .ai import analyze_symptoms
from rest_framework import status
import json
import re


# User = get_user_model() # No longer needed here

class PharmacyViewSet(viewsets.ModelViewSet):
    """
    This ViewSet is open for anyone to view pharmacies.
    """
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [permissions.AllowAny]


class MedicineViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing medicines.
    - Anyone can view the list or details of medicines (no authentication required).
    - Only authenticated users can create, update, or delete medicines.
    """

    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    # Use dynamic permissions
    def get_permissions(self):
        """
        Allow unrestricted access for read-only actions (GET, HEAD, OPTIONS),
        but require authentication for write actions (POST, PUT, PATCH, DELETE).
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        """
        Automatically set the owner to the logged-in user when creating a medicine.
        """
        serializer.save(owner=self.request.user.pharmacy)

    def get_queryset(self):
        """
        - Allow everyone to see all medicines (public view).
        - Optionally, you can uncomment the filter below if you ever want to
          restrict views to the authenticated user's medicines only.
        """
        return Medicine.objects.all()
    

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_medicines(self, request):
        """
        Returns only the medicines that belong to the pharmacy
        associated with the logged-in user.
        """
        if not request.user.pharmacy:
            return Response({"error": "You are not linked to any pharmacy."}, status=403)

        medicines = Medicine.objects.filter(owner=request.user.pharmacy)
        serializer = self.get_serializer(medicines, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([AllowAny])
def symptom_checker(request):
    symptoms = request.data.get("symptoms", "")
    if not symptoms:
        return Response({"error": "Please provide symptoms."}, status=status.HTTP_400_BAD_REQUEST)

    ai_response = analyze_symptoms(symptoms)

    # Clean the AI response to extract JSON from ```json ... ``` blocks
    json_match = re.search(r"```json(.*?)```", ai_response, re.DOTALL)
    if json_match:
        try:
            clean_json = json.loads(json_match.group(1))
            return Response(clean_json)
        except json.JSONDecodeError:
            pass

    # Fallback: try to parse the whole response
    try:
        return Response(json.loads(ai_response))
    except json.JSONDecodeError:
        return Response({"analysis": ai_response}) 

def index(request):
    return render(request, "index.html")
