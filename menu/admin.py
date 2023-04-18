from django.contrib import admin

from .models import Menu, Category


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # filter_vertical = ('parent',)
    search_fields = ['parent__id']