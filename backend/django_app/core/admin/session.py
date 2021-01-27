class SessionAdmin(admin.ModelAdmin):
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

# register SessionAdmin
admin.site.register(ParlamentSession, ParlamentSessionAdmin)