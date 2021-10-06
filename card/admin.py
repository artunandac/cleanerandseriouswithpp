from django.contrib import admin

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('cardid','owner','name','mail','company')
    list_display_links = ('cardid','owner')
    list_filter = ('cardid','owner','name','mail','company')
    search_fields = ('cardid','owner','name','mail','company','description')
    list_per_page = 20

# Register your models here.
admin.site.register(Card, CardAdmin)
