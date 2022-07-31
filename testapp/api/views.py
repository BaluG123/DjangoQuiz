from . serializers import quizSerializers
from rest_framework.viewsets import ModelViewSet
from testapp.models import Quiz
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Quiz_view(ModelViewSet):
    queryset=Quiz.objects.all()
    serializer_class=quizSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
