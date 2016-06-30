from django.contrib import admin
from .models import Post, Comment, Contact

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created', 'updated', 'status')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'sent']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
