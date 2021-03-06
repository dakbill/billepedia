from django.db import models
from django.contrib import admin
# Create your models here.
class Dakbill(models.Model):
	name=models.TextField()
	title=models.TextField()
	body=models.TextField()
	created = models.DateField(auto_now_add=True)
   	updated = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.name
class Comment(models.Model):
    body = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    dakbill = models.ForeignKey(Dakbill,related_name='Dakbill')
class DakbillAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search=('title','body')
    list_filter=('title','created')
class CommentAdmin(admin.ModelAdmin):
    list_display=('dakbill','author','body','created','updated')
    list_filter=('author','created')
admin.site.register(Dakbill,DakbillAdmin)
admin.site.register(Comment,CommentAdmin)
