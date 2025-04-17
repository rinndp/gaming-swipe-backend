from django.contrib import admin
from rest_framework.authtoken.admin import User

from users.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_name', 'updated_at', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ("is_superuser", "is_active", "is_staff")
    list_editable = ('is_staff', 'is_superuser', 'is_active',)

    search_fields = ("email","name",)
    ordering = ('-updated_at',)

admin.site.register(CustomUser, CustomUserAdmin)