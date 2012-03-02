from django.contrib import admin
from buyerguide.buyerguideapp.models import Group, Publication

class GroupAdmin(admin.ModelAdmin):
   list_display = ('name', 'email')
   search_fields = ('name', 'email')

admin.site.register(Group, GroupAdmin)
admin.site.register(Publication)

