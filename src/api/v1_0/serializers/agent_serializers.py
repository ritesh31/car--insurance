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
        fields = '__all__'

class AgentLoginSerializer(serializers.ModelSerializer):
    """
    Serializer to login agent
    """
    email = serializers.EmailField(required=True, allow_blank=False)

    class Meta:
        model = Agent
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, data):
        """
        User authentication 
        """
        print('data-------------', data)
        agent = authenticate(email=data['email'], password=data['password'])
        print('agent-------------', agent) 
        if not agent:
            raise AuthenticationFailed()
        return agent
