from django.contrib import admin

from .models import Tenant, Member

admin.site.register(Tenant)
admin.site.register(Member)
