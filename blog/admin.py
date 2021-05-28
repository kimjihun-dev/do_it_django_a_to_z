from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)


class CategoryAdmin(admin.ModelAdmin):
    # Category 모델의 name 필드 값이 입력될때 자동으로 slug 가 만들어짐
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagAdmin)