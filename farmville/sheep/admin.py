from django.contrib import admin
from farmville.sheep.models import Sheep
from farmville.location.models import Location

class SheepAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(SheepAdmin, self).queryset(request)
        return qs.filter(farmer=request.user)
    list_display = ('sheepId', 'name', 'farmer')
    
admin.site.register(Sheep, SheepAdmin)
admin.site.register(Location)
