from django.contrib import admin
from farmville.sheep.models import Sheep
from farmville.location.models import Location

class SheepAdmin(admin.ModelAdmin):

    list_display = ('sheepId', 'name', 'farmer')
    exclude = ('farmer',)

    def queryset(self, request):
        qs = super(SheepAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(farmer=request.user)

    def save_model(self, request, obj, form, change):
        obj.farmer = request.user
        obj.sheepId = obj.farmer.farmerId + obj.birthday + obj.sheepId
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == Sheep:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.farmer = request.user
                instance.sheepId = instance.farmer.farmerId + instance.sheepId
                instance.save()
        else:
            formset.save()
admin.site.register(Sheep, SheepAdmin)
admin.site.register(Location)

