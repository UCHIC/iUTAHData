from django.contrib import admin
from mdfserver.models import Page, Subpage

# Register your models here.
class SubpagesInline(admin.StackedInline):
    model = Subpage
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['title']}),
        ('Content', {'fields': ['content']}),
        #('Sub Pages', {'fields': [], 'classes':['collapse']}),
    ]
    inlines = [SubpagesInline]

admin.site.register(Page, PageAdmin)