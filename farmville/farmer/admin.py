from django.contrib import admin
from farmville.farmer.models import Farmer
from farmville.sheep.models import Sheep

class FarmerAdmin(admin.ModelAdmin):
    list_display = ('username', 'farmerId', 'first_name')
    def queryset(self, request):
        qs = super(FarmerAdmin, self).queryset(request)

        if request.user.is_superuser:
            self.exclude = {}
            return qs
        self.exclude = ['username', 'user_permissions', 'groups', 'last_login', 'password', 'staff', 'date_joined', 'is_staff', 'is_superuser', 'is_active']
        return qs.filter( username = request.user.username)
    def save_model(self, request, obj, form, change):
        if not(obj.farmerId == request.user.farmerId):
            liste = obj.own.all()
            for s in liste:
                s.sheepId = str(obj.farmerId) + s.sheepId[7:12]
                s.save()
        obj.save()

admin.site.register(Farmer, FarmerAdmin)