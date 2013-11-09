from django.contrib import admin
from farmville.message.models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('time', 'receiver', 'receiver_reserve')
    def queryset(self, request):
        qs = super(MessageAdmin, self).queryset(request)

        if request.user.is_superuser:
            self.exclude = {}
            return qs
	
        return qs.filter( receiver = request.user )

admin.site.register(Message, MessageAdmin)
