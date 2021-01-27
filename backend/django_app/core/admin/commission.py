class CommissionRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))

    class Meta:
        model = Commission
        import_id_fields = ['id']

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

# register commission
admin.site.register(Commission, CommissionAdmin)