from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["description", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["description"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["description"]


admin.site.register(Question, QuestionAdmin)