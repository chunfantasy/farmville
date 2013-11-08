from django.contrib import admin
from farmville.farmer.models import Farmer

class FarmerAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(FarmerAdmin, self).queryset(request)
<<<<<<< HEAD
        if request.user.is_superuser:
            self.exclude = {}
            return qs
=======

	if request.user.is_superuser:
            self.exclude = {}
	    return qs
>>>>>>> 0157500cbe17f6374fbf24e2ac809f8665312210
        self.exclude = ['username', 'user_permissions', 'groups', 'last_login', 'password', 'staff', 'farmerId', 'date_joined', 'is_staff', 'is_superuser', 'is_active']
        return qs.filter( username = request.user.username)
    list_display = ('username', 'farmerId', 'first_name')



admin.site.register(Farmer, FarmerAdmin)
