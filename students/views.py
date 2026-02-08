from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminOrReadOnly
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
