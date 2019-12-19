from django.contrib import admin

from .models import Seyahat,Comment
# Register your models here.
admin.site.register(Comment)

@admin.register(Seyahat)
class SeyahatAdmin(admin.ModelAdmin):

    list_display = ["title","yazar","created_date"]
    list_display_links=["title","yazar","created_date"]
    search_fields=["title"]
    class Meta:
        model = Seyahat