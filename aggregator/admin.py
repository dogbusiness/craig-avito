from django.contrib import admin
from aggregator.models import User, Category, Subcategory, Post, Media
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Post)
admin.site.register(Media)