from django.contrib import admin

# import Parlaments + depending
from legislatives.models import Parlament, ParlamentSession, ParlamentRole, ParlamentMembership, ParlamentMembershipRole
# import Commission + depending
from legislatives.models import Commission, CommissionRole, CommissionMembership, CommissionMembershipRole

from django.utils.safestring import mark_safe

# *************************************************************************************
# Parlament
# *************************************************************************************

# inline for CantonParlamentMembership
class ParlamentMembershipRoleInline(admin.TabularInline):
    model = ParlamentMembershipRole
    extra = 1

class ParlamentAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Parlament
    """
    raw_id_fields = ['city']
    readonly_fields = ['get_avatar_preview']

    fieldsets = (
        ('General Information', { 'fields': ('title', 'description', 'number_of_seats',) }),
        ('Jurisdiction (Sparse)', {'fields': ('jurisdiction_country', 'jurisdiction_canton', 'jurisdiction_municipality',)}),
        ('Address', { 'fields': ('street1', 'street2', 'city')}),
        ('Location', { 'fields': ('location_query', 'location')}),
        ('Contact', {'fields': ('email', 'website', 'phone')}),
        ('Avatar', {'fields': ('avatar', 'get_avatar_preview')}),
    )

    list_display = ('title', 'get_jurisdiction_name')
    search_fields = ['title' 'get_jurisdiction_name',]
    
    def get_jurisdiction_name(self, obj):
        # change depending on level
        if obj.jurisdiction_country != None:
            return obj.jurisdiction_country.name
        elif obj.jurisdiction_canton != None:
            return obj.jurisdiction_canton.name
        elif obj.jurisdiction_municipality != None:
            return obj.jurisdiction_municipality.name
        return "Unknown Jurisdiction"

    def get_avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-width: 150px" />')

class ParlamentSessionAdmin(admin.ModelAdmin):
    """
    Customizing admininterface for ParlamentSession
    """
    
    fieldsets = (
        ('Parlament', {'fields': ('parlament',)}),
        ('General Information', {'fields': ('date', 'opening_session', 'regular_session', 'additional_information')}),
        ('Messages', {'fields': ('greeting', 'discharge',)}),
        ('Excused Councillors', {'fields': ('excused_politicans',)})
    )

    list_display = ('parlament', 'date', 'regular_session',)


class ParlamentRoleAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for ParlamentRole
    """
    fieldsets = (
        ('General Information', {'fields': ('title', 'description')}),
        ('Belonging Parlament', {'fields': ('parlament',)})
    )

    list_display = ('title', 'parlament')

class ParlamentMembershipAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Model ParlamentMembership (+ Roles through _Inlines)
    """
    inlines = [ ParlamentMembershipRoleInline ]
    list_display = ('politican', 'parlament')


# *************************************************************************************
# Commission
# *************************************************************************************
# inline for CantonParlamentMembership
class CommissionMembershipRoleInline(admin.TabularInline):
    model = CommissionMembershipRole
    extra = 1

class CommissionAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Commission
    """
    fieldsets = (
        ('General Information', { 'fields': ('title', 'description', 'permanent', 'start_date', 'end_date',) }),
        ('Belonging Parlament', {'fields': ('parlament',)}),
        ('Contact', {'fields': ('email', 'website', 'phone')}),
    )

    list_display = ('title', 'parlament')
    search_fields = ['title' 'parlament',]

class CommissionRoleAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for CommissionRole
    """
    fieldsets = (
        ('General Information', {'fields': ('title',)}),
        ('Belonging Commission', {'fields': ('commission',)}),
    )

    list_display = ('title', 'commission')

class CommissionMembershipAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Model CommissionMembership (+ Roles through _Inlines)
    """
    inlines = [ CommissionMembershipRoleInline ]
    list_display = ('politican', 'commission')


# register parlament + depending
admin.site.register(Parlament, ParlamentAdmin)
admin.site.register(ParlamentSession, ParlamentSessionAdmin)
admin.site.register(ParlamentRole, ParlamentRoleAdmin)
admin.site.register(ParlamentMembership, ParlamentMembershipAdmin)

# register commission + depending
admin.site.register(Commission, CommissionAdmin)
admin.site.register(CommissionRole, CommissionRoleAdmin)
admin.site.register(CommissionMembership, CommissionMembershipAdmin)

