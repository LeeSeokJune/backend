from tkinter import PhotoImage
from django.contrib import admin
from .models import Product, ProductPhoto
# Register your models here.

class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoInline,]
    #list_diplay = ('p_id')
    #list_editable = ('p_brand','p_name')

admin.site.register(Product, ProductAdmin)