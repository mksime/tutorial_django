from django.contrib import admin

from .models import Question

class QuetionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuetionAdmin)