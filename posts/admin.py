from django.contrib import admin

from .models import Post, Comment

class CommentInline(admin.StackedInline):
  model = Comment
  extra = 1

class PostAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Post', { 
      'fields': ['title', 'text'],
      'classes': 'collapse'
    })
  ]
  inlines = [CommentInline]

admin.site.register(Post, PostAdmin)