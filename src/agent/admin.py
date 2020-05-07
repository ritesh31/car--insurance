from django.contrib import admin

# Register your models here.
from .models import (Agent)

class AgentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Agent, AgentAdmin)