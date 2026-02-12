from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminOrReadOnly
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer