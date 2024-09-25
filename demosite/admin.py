from django.contrib import admin
from .models import Category, Dataset, UserDataset

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class DatasetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'visibility')
    search_fields = ('title', 'description')
    list_filter = ('visibility', 'category')
    raw_id_fields = ('author',)

class UserDatasetAdmin(admin.ModelAdmin):
    list_display = ('user', 'dataset','has_access')
    search_fields = ('user__username', 'dataset__title')
    list_filter = ('has_access',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(UserDataset, UserDatasetAdmin)
