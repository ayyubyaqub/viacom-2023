from django.contrib import admin
from .models import other_services, other_services_blocks , other_services_page 

# Register your models here.
class other_services_blocks_inline(admin.TabularInline ):
    model = other_services_blocks
    extra = 1


class other_services_admin(admin.ModelAdmin):
    inlines = [other_services_blocks_inline]

admin.site.register(other_services , other_services_admin)
admin.site.register(other_services_page)
