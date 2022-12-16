from django.contrib import admin
from categories.models import Categories, CategoriesVideo, Meta_Categories, SuperCategory, YoutubeVideoLinks
from clients.models import ClientVideos, Clients
from subscription.models import Subscription
from .models import Contact_Us_Page, Home_work_youtube_video, Marketing_Page, Meta_Sub_Categories, MetaTags, Subscription_Page, TermsAndCondition, Two_Four_Seven, Two_Four_Seven_Integrated, Two_Four_Seven_Page, Academic_page, Academics, Video_Marketing, Video_Marketing_Page,  work
from home.models import Shorts , Shorts_Page , Marketing_Page , Marketing ,Media_Page ,Media,Homecarousel,Videoseeding,Videocategory,home_image,homePageHeading,homePageHeadingImage,SubCategories,Aboutus,aboutusteam,aboutusattribute,Home_page_video,about_us_youtube,work_youtube_video,create_video,create_video_image,Image_client_logo_and_Vi,MarketPlaceVideo,Customer,SuperCategoryVideo,contact_us_location,Interest_Person,creators,career_header_content , career , career_table_header
# Register your models here.

admin.site.register(SuperCategoryVideo)

admin.site.register(YoutubeVideoLinks)
admin.site.register(CategoriesVideo)

admin.site.register(Subscription)
admin.site.register(Clients)
admin.site.register(ClientVideos)
admin.site.register(Homecarousel)
admin.site.register(Videoseeding)
admin.site.register(Videocategory)
admin.site.register(home_image)
admin.site.register(homePageHeading)
admin.site.register(homePageHeadingImage)
admin.site.register(Home_work_youtube_video)


#Career
class career_header_content_inline(admin.TabularInline ):
    model = career_header_content
    extra = 4


class career_table_header_admin(admin.ModelAdmin):
    inlines = [career_header_content_inline]
    
admin.site.register(career)
admin.site.register(career_table_header , career_table_header_admin)
# admin.site.register(career_header_content)

#Media
admin.site.register(Media)
admin.site.register(Media_Page)
#Marketing
admin.site.register(Marketing)
admin.site.register(Marketing_Page)
#video Marketing
admin.site.register(Video_Marketing)
admin.site.register(Video_Marketing_Page)
#Shorts
admin.site.register(Shorts)
admin.site.register(Shorts_Page)
#Academic
admin.site.register(Academics)
admin.site.register(Academic_page)

#24x7
admin.site.register(Two_Four_Seven)
admin.site.register(Two_Four_Seven_Page)
admin.site.register(Two_Four_Seven_Integrated)

admin.site.register(Aboutus)
admin.site.register(aboutusteam)
admin.site.register(aboutusattribute)
admin.site.register(Home_page_video)
admin.site.register(work)          
admin.site.register(about_us_youtube)
admin.site.register(work_youtube_video)
admin.site.register(create_video)
admin.site.register(create_video_image)
admin.site.register(Image_client_logo_and_Vi)
admin.site.register(MarketPlaceVideo)
admin.site.register(TermsAndCondition)
admin.site.register(contact_us_location)
admin.site.register(Contact_Us_Page)
admin.site.register(Interest_Person)
admin.site.register(creators)
admin.site.register(Customer)

admin.site.register(Subscription_Page)

@admin.register(MetaTags)
class MetaTagsAdmin(admin.ModelAdmin):
    search_fields = ('meta_name','categories', 'subcategories','meta_description')
    list_display = ('meta_name','categories', 'subcategories')


    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(MetaTagsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'subcategories':
            field.queryset = SubCategories.objects.all().order_by('subcategory')
        if db_field.name == 'categories':
            field.queryset = Categories.objects.all().order_by('category')
        return field


class Meta_Categories_inline(admin.TabularInline ):
    model = Meta_Categories
    extra = 1

# @admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('category','slug', 'price','brief')
    list_display = ('category','slug', 'price','brief')
    list_filter = ['super_category']
    inlines = [Meta_Categories_inline]

admin.site.register(Categories , CategoriesAdmin)


@admin.register(SuperCategory)
class SuperCategoryAdmin(admin.ModelAdmin):
    search_fields = ('super_category_name','slug', 'description')
    list_display = ('super_category_name','slug', 'description')

class Meta_Sub_Categories_inline(admin.TabularInline ):
    model = Meta_Sub_Categories
    extra = 1

# @admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    search_fields = ('subcategory','slug')
    list_display = ('subcategory','slug', 'category_','is_active')
    list_filter = ['category']
    inlines = [Meta_Sub_Categories_inline]
    def category_(self, obj):
        return "\n".join([c.slug for c in obj.category.all()])


admin.site.register(SubCategories , SubCategoriesAdmin)