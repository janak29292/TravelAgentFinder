from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Payment ,Agent, Client
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Payment)
admin.site.register(Agent)
admin.site.register(Client)
