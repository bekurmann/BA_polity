from django.contrib import admin

# import models
from legislatives.models import ( Parlament, ParlamentSession, ParlamentMembership,
                                Commission, CommissionMembership )
from politicans.models import Politican
from locations.models import Country, Canton, Municipality, PLZ

# avatar preview
from django.utils.safestring import mark_safe

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# *************************************************************************************
# import export ressources
# *************************************************************************************

class ParlamentRessource(resources.ModelResource):
    city= fields.Field(column_name='city', attribute='city', widget=ForeignKeyWidget(PLZ, 'pk'))
    jurisdiction_country = fields.Field(column_name='jurisdiction_country', attribute='jurisdiction_country',
                            widget=ForeignKeyWidget(Country, 'pk'))
    jurisdiction_canton = fields.Field(column_name='jurisdiction_canton', attribute='jurisdiction_canton',
                            widget=ForeignKeyWidget(Canton, 'pk'))
    jurisdiction_municipality = fields.Field(column_name='jurisdiction_municipality', attribute='jurisdiction_municipality',
                            widget=ForeignKeyWidget(Municipality, 'pk'))

    class Meta:
        model = Parlament
        import_id_fields = ['id']

class ParlamentMembershipRessource(resources.ModelResource):
    politican = fields.Field(column_name='politican', attribute='politican', widget=ForeignKeyWidget(Politican, 'pk'))
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))

    class Meta:
        model = ParlamentMembership
        import_id_fields = ['id']

class CommissionRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))

    class Meta:
        model = Commission
        import_id_fields = ['id']

# *************************************************************************************
# Parlament Admin
# *************************************************************************************

class ParlamentAdmin(ImportExportModelAdmin):
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

    resource_class = ParlamentRessource

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


class ParlamentMembershipAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Model ParlamentMembership
    """
    raw_id_fields = ['politican']
    readonly_fields = ('active',)

    fieldsets = (
        ('Membership Type', {'fields': ('membership_type',)}),
        ('Foreign Keys', {'fields': ('politican', 'parlament', )}),
        ('Start- Enddate', {'fields': ('start_date', 'end_date',)}),
        ('Active (Calculated)', {'fields': ('active',)}),
    )

    resource_class = ParlamentMembershipRessource

    list_display = ('politican', 'membership_type', 'parlament', 'active',)


# *************************************************************************************
# Commission Admin
# *************************************************************************************

class CommissionAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Commission
    """
    fieldsets = (
        ('General Information', { 'fields': ('title', 'description', 'permanent', 'start_date', 'end_date',) }),
        ('Belonging Parlament', {'fields': ('parlament',)}),
        ('Contact', {'fields': ('email', 'website', 'phone')}),
    )

    resource_class = CommissionRessource

    list_display = ('title', 'parlament')
    search_fields = ['title' 'parlament',]


class CommissionMembershipAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Model CommissionMembership
    """
    raw_id_fields = ['politican']
    readonly_fields = ('active',)

    fieldsets = (
        ('Membership Type', {'fields': ('membership_type',)}),
        ('Foreign Keys', {'fields': ('politican', 'commission', )}),
        ('Start- Enddate', {'fields': ('start_date', 'end_date',)}),
        ('Active (Calculated)', {'fields': ('active',)}),
    )

    list_display = ('politican', 'commission')


# register parlament + depending
admin.site.register(Parlament, ParlamentAdmin)
admin.site.register(ParlamentSession, ParlamentSessionAdmin)
admin.site.register(ParlamentMembership, ParlamentMembershipAdmin)

# register commission + depending
admin.site.register(Commission, CommissionAdmin)
admin.site.register(CommissionMembership, CommissionMembershipAdmin)

