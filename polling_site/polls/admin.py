from django.contrib import admin

#Bringing in our models, so we can see it in the admin area
from .models import Question, Choice                        

#Changing the Header information from default values
admin.site.site_header = "Polling Site Admin"
admin.site.site_title = "Polling Site Admin Area"
admin.site.index_title = "Welcome to the Admin Area"

# admin.site.register(Question)
# admin.site.register(Choice)

# The code in documentation displays choices in a different tab not linked to the questions in the admin area, 
# while I want the choices to be displayed under it's respective question
# So, I am leveraging the TabularInLine class which comes packed with the admin.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), 
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)