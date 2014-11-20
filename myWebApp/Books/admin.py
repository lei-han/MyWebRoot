from django.contrib import admin
from Books.models import Publisher, Author, Book
from django.contrib.admin.templatetags.admin_list import date_hierarchy

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','email')
    search_fields = ('firstName','lastName')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publicationDate')
    list_filter = ('publicationDate','author','publisher',)
    date_hierarchy = 'publicationDate'
    ordering = ('-publicationDate','title',)
    #fields = ('title','author','publisher')
    filter_horizontal = ('author',)
    #raw_id_fields=('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


