from rest_framework.generics import (CreateAPIView, ListCreateAPIView)
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from knox.views import LoginView as KnoxLoginView
from agent.models import Agent
from api.v1_0.serializers.agent_serializers import (AgentSerializer, AgentLoginSerializer)

class AgentView(CreateAPIView):
    """
    Agent View Set for create agent
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentLoginView(ListCreateAPIView):
    """
    Agent View Set for login agent
    """
    # queryset = Agent.objects.all()
    serializer_class = AgentLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AgentLoginSerializer(data=request.data)
        print('inisde view-----------', serializer)
        serializer.is_valid(raise_exception=True)
        agent = serializer.validated_data
        login(request, agent)
        return KnoxLoginView().post(request, format=None)