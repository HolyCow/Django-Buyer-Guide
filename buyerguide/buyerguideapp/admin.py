from django.contrib import admin
from buyerguide.buyerguideapp.models import Group, Publication

class GroupAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'join_date')
   search_fields = ('name', 'email')
   list_filter = ('join_date',)
   date_hierarchy = 'join_date'
   ordering = ('name',)

admin.site.register(Group, GroupAdmin)
admin.site.register(Publication)

