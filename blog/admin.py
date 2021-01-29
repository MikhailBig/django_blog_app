from django.contrib import admin
from django.contrib.admin.options import IncorrectLookupParameters
from .models import Post
admin.site.register(Post)

