from django.contrib import admin
from .models import Vi_Network , Vi_Network_card,Vi_Network_Page

# Register your models here.
class vi_network_card_inline(admin.TabularInline ):
    model = Vi_Network_card
    extra = 1


class vi_network_admin(admin.ModelAdmin):
    inlines = [vi_network_card_inline]

admin.site.register(Vi_Network_Page)
admin.site.register(Vi_Network , vi_network_admin)