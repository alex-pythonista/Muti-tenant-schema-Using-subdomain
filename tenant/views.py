from django.shortcuts import render

from .models import Member

from .utilities import get_tenant

def our_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)

    context = {'tenant': tenant, 'members': members}

    return render(request, 'index.html', context)
