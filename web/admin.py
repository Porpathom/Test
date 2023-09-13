from django.contrib import admin
from web.models import Subj, Cate
# Register your models here.

@admin.register(Subj)
class SubjAdmin(admin.ModelAdmin):
    list_display= ['subj_code', 'subj_name', 'semester', 'year','cate', 'credit' ]

@admin.register(Cate)
class CateAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    
