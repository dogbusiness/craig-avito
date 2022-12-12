from django.contrib import admin
from aggregator.models import UserProfile, Category, Subcategory, Post, Media
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Post)
admin.site.register(Media)