from django.contrib import admin
from geographyquiz.models import Questions, Answers

class AnswersInline(admin.StackedInline):
    model = Answers
    extra = 0

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswersInline]

admin.site.register(Questions, QuestionsAdmin)
##admin.site.register(Answers, AnswersAdmin)


