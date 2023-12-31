from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationFrom, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFrom
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)    