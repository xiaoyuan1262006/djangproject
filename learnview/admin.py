from django.contrib import admin
from .models import *
# Register your models here.
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields =  ['btitle']
    list_per_page =  2
    fieldsets = [('base',{'fields':['btitle']}),
                 ('super',{'fields':['bpub_date']})]
    inlines = [HeroInfoInline]


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender','hcontent','hbooke']
    list_filter = ['hname']
    search_fields = ['hname']
    list_per_page = 2


#admin.site.register(BookInfo,BookInfoAdmin)
#admin.site.register(HeroInfo,HeroInfoAdmin)
