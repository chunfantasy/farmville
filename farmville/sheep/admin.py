# -*- coding: utf-8 -*-
from django.contrib import admin
from farmville.sheep.models import Sheep
from farmville.location.models import Location

class SheepAdmin(admin.ModelAdmin):

    list_display = ('birthday','sheepId', 'name', 'farmer')
    exclude = ('farmer',)

    def queryset(self, request):
        qs = super(SheepAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(farmer=request.user)

    def save_model(self, request, obj, form, change):
        obj.farmer = request.user
        birthyear = str(obj.birthday)[3]
        if (len(str(obj.sheepId)) == 12):
            if (obj.sheepId[0:6] != obj.farmer.farmerId.zfill(7) or obj.sheepId[8] != birthyear):
                obj.sheepId = obj.farmer.farmerId.zfill(7) + birthyear + obj.sheepId[8:12]
        if (len(str(obj.sheepId)) == 4):
            obj.sheepId = obj.farmer.farmerId.zfill(7) + birthyear + obj.sheepId

        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == Sheep:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.farmer = request.user
                if(instance.sheepId == 4):
                    instance.sheepId = instance.farmer.farmerId + instance.sheepId
                instance.save()
        else:
            formset.save()
admin.site.register(Sheep, SheepAdmin)
admin.site.register(Location)

