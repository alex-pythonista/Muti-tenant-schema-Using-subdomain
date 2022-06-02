from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)


class Member(TenantAwareModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name