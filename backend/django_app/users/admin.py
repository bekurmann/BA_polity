from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

# for avatar_preview
from django.utils.safestring import mark_safe

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    """
    Customizing Admininterface for Custom User Model
    """
    readonly_fields = ['get_avatar_preview']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'bio', 'date_of_birth',)}),
        ('Location', {'fields': ('location_query', 'location', )}),
        ('Contact', {'fields': ('website', )}),
        ('Avatar', {'fields': ('avatar', 'get_avatar_preview')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets: these fields will be shown when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('username', 'email',)

    def get_avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-width: 150px" />')


admin.site.register(CustomUser, CustomUserAdmin)

# unregister sites, groups
admin.site.unregister(Group)
admin.site.unregister(Site)
#admin.site.unregister()