class PoliticanRessource(resources.ModelResource):
    city = fields.Field(column_name='jurisdiction', attribute='city',
                        widget=ForeignKeyWidget(PLZ, 'name'))

    class Meta:
        model = Politican
        import_id_fields = ['id']

# *****************************************************************************************
# admin models
# *****************************************************************************************
class PoliticanAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Politican
    """
    raw_id_fields = ['city']
    readonly_fields = ['get_avatar_preview']

    fieldsets = (
        ('Personal Information', { 'fields': ('first_name', 'last_name', 'title', 'profession', 'date_of_birth',) }),
        ('Address', { 'fields': ('street1', 'street2', 'city',) }),
        ('Location', { 'fields': ('location_query', 'location',  ) }),
        ('Contact', { 'fields': ('email', 'website', 'phone' ) }),
        ('Avatar', { 'fields': ('avatar', 'get_avatar_preview', ) }),
    )

    resource_class = PoliticanRessource

    list_display = ('first_name', 'last_name', 'get_city_name',)
    search_fields = ['first_name' 'last_name', 'get_city_name',]

    # function for getting the city name (foreign key PLZ, field "name")
    def get_city_name(self, obj):
        return obj.city.name

    def get_avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-width: 150px" />')

admin.site.register(Politican, PoliticanAdmin)