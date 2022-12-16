from django.contrib import admin

from dare2creative.models import Category, D2C_Page, D2C_Posters, Sub_Category, Super_Category


class category_inline(admin.TabularInline ):
    model = Category
    extra = 2


class super_category_admin(admin.ModelAdmin):
    fieldsets = [
        ('Super Category',{'fields': ['title' , 'description']}),
    ]
    inlines = [category_inline]


#Posters 1st one
class poster_inline(admin.TabularInline ):
    model = D2C_Posters
    extra = 3
    
class d2c_posters_admin(admin.ModelAdmin):
    inlines = [poster_inline]

admin.site.register(D2C_Page , d2c_posters_admin)
admin.site.register(Sub_Category)
admin.site.register(Super_Category , super_category_admin)

