from django.contrib import admin

from parties.models import Party, PartyFunction

class PartyAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Model Council
    """
    list_display = ('name', 'abbreviation',)

class PartyFunctionAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Model CouncilFunction
    """
    list_display = ('title',)

admin.site.register(Party, PartyAdmin)
admin.site.register(PartyFunction, PartyFunctionAdmin)
