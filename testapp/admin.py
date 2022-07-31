from django.contrib import admin
from . models import Quiz

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display=['id','question','option1','option2','option3','option4']
    list_filter=['created','updated','question']
    search_fields=('question','option1','option2','option3','option4')

admin.site.register(Quiz,QuizAdmin)    