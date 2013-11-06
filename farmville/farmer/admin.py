from django.contrib import admin
from farmville.farmer.models import Farmer

class FarmerAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(FarmerAdmin, self).queryset(request)
	if request.user.username == 'a':
	    return qs
        return qs.filter( username = request.user.username)
    list_display = ('username', 'farmerId', 'first_name')
    

admin.site.register(Farmer, FarmerAdmin)
