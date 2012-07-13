from blog.models import Comment,Dakbill
from django.contrib import admin

class DakbillAdmin(admin.ModelAdmin):
    list_display('title','date_created','date_updated')
    search('title','body')
    list_filter('title','date_created')

class CommentAdmin(admin.ModelAdmin):
    list_display('Dakbill','author','body','created','date_updated')
    list_filter('author','created')
class CommentInline(admin.TabularInline):
  model=Comment
admin.site.register(Dakbill,DakbillAdmin)
admin.site.register(Comment,CommentAdmin)
    
    
