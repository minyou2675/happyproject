from django.contrib import admin
from .models import Post, Tag, Category, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',) }
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment)