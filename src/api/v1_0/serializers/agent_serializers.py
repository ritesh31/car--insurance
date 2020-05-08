from agent.models import Agent
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer to create agent
    """
    class Meta:
        model = Agent
        fields = ('id', 'email', 'password')
    
    def create(self, validated_data):
        print('validated_data------------------', validated_data)
        agent = super().create(validated_data)
        agent.set_password(agent.password)
        agent.save()
        return agent

class AgentLoginSerializer(serializers.ModelSerializer):
    """
    Serializer to login agent
    """
    email = serializers.EmailField(required=True, allow_blank=False)

    class Meta:
        model = Agent
        fields = ('email', 'password')

    def validate(self, data):
        """
        User authentication 
        """
        agent = authenticate(email=data['email'], password=data['password'])
        if not agent:
            raise AuthenticationFailed()
        return agent
