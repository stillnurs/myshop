from django.contrib import admin
from .models import Category, Product


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'status', 'price']
	prepopulated_fields = {'slug': ('name',)}


