# apps/pharmacies/views.py

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
# We don't need these for the secure version
# from rest_framework.exceptions import ValidationError
# from django.contrib.auth import get_user_model
from .models import Pharmacy, Medicine
from .serializers import PharmacySerializer, MedicineSerializer
from django.shortcuts import render


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
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        - Allow everyone to see all medicines (public view).
        - Optionally, you can uncomment the filter below if you ever want to
          restrict views to the authenticated user's medicines only.
        """
        return Medicine.objects.all()
    

     # ✅ NEW: Only logged-in user's medicines
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_medicines(self, request):
        """
        Returns only the medicines created/owned by the logged-in user.
        """
        medicines = Medicine.objects.filter(owner=request.user)
        print(request.user.email)
        serializer = self.get_serializer(medicines, many=True)
        return Response(serializer.data)

def index(request):
    return render(request, "index.html")
