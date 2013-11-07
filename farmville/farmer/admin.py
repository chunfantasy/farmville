from django.contrib import admin
from farmville.farmer.models import Farmer

class FarmerAdmin(admin.ModelAdmin):
    def queryset(self, request):
        qs = super(FarmerAdmin, self).queryset(request)
	if request.user.is_superuser:
		self.exclude = {}
	    return qs
	self.exclude = ['username', 'user_permissions', 'groups', 'last_login', 'password', 'staff', 'farmerId', 'date_joined', 'is_staff', 'is_superuser', 'is_active']
        return qs.filter( username = request.user.username)
    list_display = ('username', 'farmerId', 'first_name')
    

admin.site.register(Farmer, FarmerAdmin)
