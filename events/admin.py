from django.contrib import admin

from events.models import Category


class CateroryAdmin(admin.ModelAdmin):
    actions = None


admin.site.register(Category, CateroryAdmin)
