from django.contrib import admin
from .models import Masseur, Img, MassageProduct, PostDetail, PolishCV

def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate.short_description = "Skopjuj wybrane rekordy"

class AdminMassageProduct(admin.ModelAdmin):
    actions = [duplicate]

class AdminPostDetail(admin.ModelAdmin):
    actions = [duplicate]

# Register your models here.
admin.site.register(Masseur)
admin.site.register(Img)
admin.site.register(MassageProduct, AdminMassageProduct)
admin.site.register(PostDetail, AdminPostDetail)
admin.site.register(PolishCV)