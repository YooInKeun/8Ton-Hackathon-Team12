from django.contrib import admin
from .models import *

admin.site.register(Message)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)