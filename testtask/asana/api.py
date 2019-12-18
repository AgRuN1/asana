from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotAuthenticated
from .serializers import TaskSerializer
from .models import Task

class TasksView(ModelViewSet):
    queryset = {}
    serializer_class = TaskSerializer

    @action(detail=False)
    def all(self, request):
        try:
            token = Token.objects.get(key=request.GET.get('token',''))
        except:
            raise NotAuthenticated('Incorrect token')

        data = Task.objects.filter(user=token.user)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)