from .models import Tenant

def get_hostname(request):
    return request.get_hostname().split(':')[0].lowser()

def get_tenant(request):
    hostname = get_hostname(request)
    subdomain = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain=subdomain).first()