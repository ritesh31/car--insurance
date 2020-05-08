from rest_framework.generics import (RetrieveAPIView, ListCreateAPIView, GenericAPIView, CreateAPIView)
from rest_framework import viewsets
from django.contrib.auth import login
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from knox.views import LoginView as KnoxLoginView
from agent.models import Agent
from api.v1_0.serializers.agent_serializers import (AgentSerializer, AgentLoginSerializer)

class AgentView(CreateAPIView):
    """
    Agent View Set for create agent
    """
    serializer_class = AgentSerializer

class AgentLoginView(GenericAPIView):
    """
    Agent View Set for login agent
    """
    serializer_class = AgentLoginSerializer

    def post(self, request):
        serializer = AgentLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        agent = serializer.validated_data
        login(request, agent)
        return KnoxLoginView().post(request, format=None)