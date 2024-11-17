from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup


class MenulinkInline(admin.StackedInline): 
    model = MenuLink
    extra = 1
        
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenulinkInline,
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
    
    

    
